#with the help of get_attribute method we can get the value of an web page element attribute.
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class getattribute(object):
    def text(self):
        driver=webdriver.Firefox()
        baseurl='https://learn.letskodeit.com/p/practice'
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(20)
        classelement=driver.find_element(By.ID,'opentab')
        classvalue=classelement.get_attribute('class')
        print ("The value of the class in the opentab element on practice page is:",classvalue)
        time.sleep(2)
        driver.quit()
g=getattribute()
g.text()
