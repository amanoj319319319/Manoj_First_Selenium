from selenium import webdriver
import random

import time
url="https://www.facebook.com/"
driver=webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(6)
driver.find_element_by_id("email").send_keys()
driver.find_element_by_id("pass").send_keys()
driver.find_element_by_name("login").click()
time.sleep(5)

#def random_generator(size=8,chars=string.ascii_lowercaase)
