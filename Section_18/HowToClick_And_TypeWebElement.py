from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Firefox()
driver.maximize_window()
baseurl="https://learn.letskodeit.com/p/practice"
driver.get(baseurl)
driver.implicitly_wait(10)
loginid=driver.find_element(By.XPATH,'//div[@id="navbar"]//a[@href="/sign_in"]')
loginid.click()
emailfield=driver.find_element(By.XPATH,'//input[@id="user_email"]')
emailfield.send_keys("test")
passwordfield=driver.find_element(By.XPATH,'//input[@id="user_password"]')
passwordfield.send_keys("test")
time.sleep(3)
emailfield.clear()
time.sleep(3)
emailfield.send_keys("testing")