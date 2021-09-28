from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
import time
import os
import re
import datetime
import chromedriver_autoinstaller


class NcuCprCrawler:
    def __init__(self, config):
        chromedriver_autoinstaller.install()

        self.config = config

        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument("--headless")
        self.chrome_options.add_argument("--disable-gpu")
        self.chrome_options.add_experimental_option(
            "excludeSwitches", ["enable-logging"])

    def get_date_data(self, driver):
        for week in range(1, 7):
            for date in range(1, 8):
                try:
                    data = WebDriverWait(driver, 1).until(EC.presence_of_element_located(
                        (By.XPATH, f"/html/body/div[2]/div[1]/div[1]/div[2]/div/table/tbody/tr/td/div/div/div[{week}]/div[2]/table/tbody/tr/td[{date}]")))

                    people_string = data.find_element_by_xpath(
                        "./a/div/span[2]")
                    people_info = re.search(r'(\d+)/(\d+)', people_string.text)
                except:
                    pass

    def fetch_status(self):
        # To see if some event is still available.
        driver = webdriver.Chrome(options=self.chrome_options)
        driver.get(self.config['BOT']['url'])

        confirm_button = WebDriverWait(driver, 1).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "body > div.col-md-12.center-block > form > button")))
        confirm_button.click()

        next_button = WebDriverWait(driver, 1).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#calendar > div.fc-toolbar > div.fc-right > div > button.fc-next-button.fc-button.fc-state-default.fc-corner-right > span")))

        for i in range(4):
            if i != 0:
                next_button.click()
            self.get_date_data(driver)

    def screenshot(self, driver):
        file_path = os.getcwd() + '\\' + "out" + '\\'

        try:
            if not os.path.exists(file_path):
                os.makedirs(file_path)
        except BaseException as msg:
            print(f"Create directory failed：{msg}")

        def S(X): return driver.execute_script(
            'return document.body.parentNode.scroll'+X)
        
        driver.set_window_size(S('Width'), S('Height'))
        driver.save_screenshot(file_path + f'result-{int(time.time())}.png')

    def run(self):
        driver = webdriver.Chrome(options=self.chrome_options)
        driver.minimize_window()
        driver.get(self.config['BOT']['url'])

        confirm_button = WebDriverWait(driver, 1).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "body > div.col-md-12.center-block > form > button")))
        confirm_button.click()

        available_events_element = WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#event")))
        available_events = available_events_element.text.split('\n')

        print(
            f"{datetime.datetime.now()} - available_events: {len(available_events)} with option: {available_events[0]}")

        # if len(available_events) <= 1 and available_events[0] == "":
        #     driver.quit()
        # else:
        #     name = WebDriverWait(driver, 1).until(
        #         EC.element_to_be_clickable((By.CSS_SELECTOR, "#name")))
        #     name.send_keys(self.config['DATA']['name'])

        #     email = WebDriverWait(driver, 1).until(
        #         EC.element_to_be_clickable((By.CSS_SELECTOR, "#email")))
        #     email.send_keys(self.config['DATA']['email'])

        #     student_id = WebDriverWait(driver, 1).until(
        #         EC.element_to_be_clickable((By.CSS_SELECTOR, "#ID")))
        #     student_id.send_keys(self.config['DATA']['student_id'])

        #     department = WebDriverWait(driver, 1).until(
        #         EC.element_to_be_clickable((By.CSS_SELECTOR, "#department")))
        #     department.send_keys(self.config['DATA']['department'])

        #     student_class = WebDriverWait(driver, 1).until(
        #         EC.element_to_be_clickable((By.CSS_SELECTOR, "#class")))
        #     student_class.send_keys(self.config['DATA']['student_class'])

        #     phone = WebDriverWait(driver, 1).until(
        #         EC.element_to_be_clickable((By.CSS_SELECTOR, "#phone")))
        #     phone.send_keys(self.config['DATA']['phone'])

        #     available_events_selector = Select(WebDriverWait(driver, 1).until(
        #         EC.element_to_be_clickable((By.CSS_SELECTOR, "#event"))))
        #     available_events_selector.select_by_index(0)

        #     submit = WebDriverWait(driver, 1).until(EC.element_to_be_clickable(
        #         (By.CSS_SELECTOR, "body > div:nth-child(2) > div.col-xs-5.container.well > form > button")))
        #     submit.click()
        if True:
            name = WebDriverWait(driver, 1).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "#name")))
            name.send_keys(self.config['DATA']['name'])

            email = WebDriverWait(driver, 1).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "#email")))
            email.send_keys(self.config['DATA']['email'])

            student_id = WebDriverWait(driver, 1).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "#ID")))
            student_id.send_keys(self.config['DATA']['student_id'])

            department = WebDriverWait(driver, 1).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "#department")))
            department.send_keys(self.config['DATA']['department'])

            student_class = WebDriverWait(driver, 1).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "#class")))
            student_class.send_keys(self.config['DATA']['student_class'])

            phone = WebDriverWait(driver, 1).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "#phone")))
            phone.send_keys(self.config['DATA']['phone'])

            self.screenshot(driver)

            driver.quit()
            exit(0)
