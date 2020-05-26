#HOW TO FIND CSS SELECTORS IN DIFFERENT WAYS
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Listofelements():
    def List(self):
        driver=webdriver.Firefox()
        baseurl='https://learn.letskodeit.com/p/practice'
        driver.get(baseurl)
        driver.maximize_window()
        driver.implicitly_wait(10)

        driver.find_element(By.CSS_SELECTOR, 'input[id="name"]')
        #the below two paths are works for only IDS
        driver.find_element(By.CSS_SELECTOR, '#name')
        driver.find_element(By.CSS_SELECTOR, 'input#name')

        driver.find_element(By.CSS_SELECTOR, 'input[class="inputs displayed-class"]')
        # the below two paths are works for only IDS
        #below two types takes only single class name value
        driver.find_element(By.CSS_SELECTOR, '.displayed-class')
        driver.find_element(By.CSS_SELECTOR, 'input.displayed-class')

        #how to append the classes until finding an unique element
        driver.find_element(By.CSS_SELECTOR, '.inputs.displayed-class')

        #below paths are works for any locaters
        driver.find_element(By.CSS_SELECTOR, 'input[id^="name"]')
        driver.find_element(By.CSS_SELECTOR, 'input[name^="enter-name"]')
        driver.find_element(By.CSS_SELECTOR, 'input[name$="-name"]')
        driver.find_element(By.CSS_SELECTOR, 'input[name$="nter-name"]')

        #how to find the child nodes
        #it works only for IDS and CLASSES
        driver.find_element(By.CSS_SELECTOR, 'fieldset>input#name')
        driver.find_element(By.CSS_SELECTOR, 'fieldset>input.displayed-class')

l=Listofelements()
l.List()
'''






