#with the help of text property we can get the text of an web paeg element
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class gettext(object):
    def text(self):
        driver=webdriver.Firefox()
        baseurl='https://learn.letskodeit.com/p/practice'
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(20)
        textelement=driver.find_element(By.ID,'opentab')
        elementtext=textelement.text
        print ("The text of the open tab element on practice page is:",elementtext)
        time.sleep(2)
        driver.quit()
g=gettext()
g.text()

