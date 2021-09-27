from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
import time
import configparser
import os
import sys
import threading
import re


def get_date_data(driver):
    for week in range(1, 7):
        for date in range(1, 8):
            try:
                data = WebDriverWait(driver, 1).until(EC.presence_of_element_located(
                    (By.XPATH, f"/html/body/div[2]/div[1]/div[1]/div[2]/div/table/tbody/tr/td/div/div/div[{week}]/div[2]/table/tbody/tr/td[{date}]")))

                people_string = data.find_element_by_xpath("./a/div/span[2]")
                people_info = re.search(r'(\d+)/(\d+)', people_string.text)
            except:
                pass


def crawl_status():
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--headless")
    chrome_options.add_experimental_option(
        "excludeSwitches", ["enable-logging"])   # disable some hardware logs

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://health.ncu.edu.tw:3001/")

    confirm_button = WebDriverWait(driver, 1).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "body > div.col-md-12.center-block > form > button")))
    confirm_button.click()

    next_button = WebDriverWait(driver, 1).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "#calendar > div.fc-toolbar > div.fc-right > div > button.fc-next-button.fc-button.fc-state-default.fc-corner-right > span")))

    for i in range(4):
        if i != 0:
            next_button.click()
        get_date_data(driver)


def crawl():
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--headless")
    chrome_options.add_experimental_option(
        "excludeSwitches", ["enable-logging"])   # disable some hardware logs

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://health.ncu.edu.tw:3001/")

    confirm_button = WebDriverWait(driver, 1).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "body > div.col-md-12.center-block > form > button")))
    confirm_button.click()

    available_confs = WebDriverWait(driver, 1).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#event")))
    available_conf_length = available_confs.text.split('\n')

    print(f"available_confs: {len(available_conf_length)}")

    if len(available_conf_length) <= 1:
        driver.quit()
    else:
        name = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#name")))
        name.send_keys("吳星翰")

        email = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#email")))
        email.send_keys("xyphuzwu@gmail.com")

        student_id = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#ID")))
        student_id.send_keys("107502576")
        
        department = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#department")))
        department.send_keys("資工")
        
        student_class = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#class")))
        student_class.send_keys("4B")
        
        phone = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#phone")))
        phone.send_keys("0908084433")

        available_confs = Select(WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#event"))))
        available_confs.select_by_index(1)

        submit = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div:nth-child(2) > div.col-xs-5.container.well > form > button")))
        submit.click()

        try:
            # kill the process
            os.system("taskkill /im chromedriver.exe /f")
            time.sleep(1)
        except:
            pass
        # Exit
        # exit(0)


if __name__ == "__main__":
    crawl()
