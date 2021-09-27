from ncu_cpr_crawler import NcuCprCrawler
import time
import configparser

if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read('config.ini')

    ncuCprCrawler = NcuCprCrawler(config)

    while True:
        ncuCprCrawler.run()
        time.sleep(int(config['BOT']['interval']))