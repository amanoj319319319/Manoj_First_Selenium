#how to get the text of an element which is in between >text<
'''
from selenium import webdriver
from selenium.webdriver.common.by import By

import time


class GetText():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(baseUrl)

        openTabElement = driver.find_element(By.ID, "opentab")
        elementText = openTabElement.text
        print("Text on element is: " + elementText)
        time.sleep(1)
        driver.quit()


ff = GetText()
ff.test()
'''

#how to get the value of an attribute
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class GetAttribute():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(baseUrl)

        element = driver.find_element_by_id("name")
        result = element.get_attribute("type")

        print("Value of attribute is: " + result)
        time.sleep(1)
        driver.quit()


ff = GetAttribute()
ff.test()

'''

'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class value_attribute():
    def value(self):
        driver=webdriver.Firefox()
        baseurl='https://learn.letskodeit.com/p/practice'
        driver.get(baseurl)
        driver.maximize_window()
        driver.implicitly_wait(10)

        element=driver.find_element(By.ID, "name")
        value=element.get_attribute("name")
        print ("value of an attribute is :",value)
v=value_attribute()
v.value()
'''






