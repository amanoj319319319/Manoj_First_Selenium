from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Firefox()
baseurl='https://learn.letskodeit.com/p/practice'
driver.get(baseurl)
bmwradiobutton1=driver.find_element(By.XPATH,'//input[@id="bmwradio"]')
bmwradiobutton1.click()
time.sleep(2)
benzradiobutton2=driver.find_element(By.XPATH,'//input[@id="benzradio"]')
benzradiobutton2.click()
time.sleep(2)
bmwcheckbox1=driver.find_element(By.XPATH,'//input[@id="bmwcheck"]')
bmwcheckbox1.click()
time.sleep(2)
benzcheckbox2=driver.find_element(By.XPATH,'//input[@id="benzcheck"]')
benzcheckbox2.click()
time.sleep(2)
print ("is bmw radio button is selected?",bmwradiobutton1.is_selected())
print ("is benz radio button is selected?",benzradiobutton2.is_selected())
print ("is bmw check box is selected?",bmwcheckbox1.is_selected())
print ("is benz check box is selected?",benzcheckbox2.is_selected())
