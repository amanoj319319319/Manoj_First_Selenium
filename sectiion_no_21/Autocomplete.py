from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class autocompleteselection(object):
    def autocomplete(self):
        driver=webdriver.Firefox()
        driver.maximize_window()
        baseurl='https://www.google.com/'
        driver.get(baseurl)
        driver.implicitly_wait(10)

        search_box=driver.find_element(By.CSS_SELECTOR, '#tsf > div:nth-child(2) > div > div.RNNXgb > div > div.a4bIc > input')
        search_box.send_keys('python')
        time.sleep(3)

        itemto_select=driver.find_element(By.CSS_SELECTOR, '#tsf > div:nth-child(2) > div > div.UUbT9 > div.aajZCb > ul > li:nth-child(3) > div.sbtc > div > span')
        itemto_select.click()
        time.sleep(2)


aa=autocompleteselection()
aa.autocomplete()