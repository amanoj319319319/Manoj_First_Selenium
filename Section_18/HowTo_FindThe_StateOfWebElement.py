from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Firefox()
baseurl='https://www.google.com/'
driver.maximize_window()
driver.get(baseurl)
driver.implicitly_wait(5)
el=driver.find_element(By.XPATH,'//input[@role="combobox"]')
e1state=el.is_enabled()
print ("is e1 enabled?",e1state)
el.send_keys("about selenium in python")
el.submit()

#This lectute is about state of an webelement whether it is enabled or disabled
#how can we know the web element is enabled or disabled
#in the html dom we will findout this ,when you inspect any element , it gives html dom right
#inside of an html dom , if they mentioned disabled for the particular element ,we cant do ,
#any operations on that particular element .
#if element is enabled ,we can do operations on that .
