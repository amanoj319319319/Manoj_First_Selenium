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

        # this css locater value is for Switch To Alert Example on the practice page
        #element=driver.find_element_by_css_selector("input#name")
        #element.send_keys("hi")

        # this css locater value is for Switch To Alert Example on the practice page
        #element1=driver.find_element(By.CSS_SELECTOR, 'input[id="name"]')
        #element1.send_keys("hi")

        # this css locater value is for Switch To Alert Example on the practice page
        #element2=driver.find_element(By.CSS_SELECTOR, "#name")
        #element2.send_keys("hi")

        # this css locater value is for Switch To Alert Example on the practice page
        #element3=driver.find_element(By.CSS_SELECTOR, 'input[name="enter-name"]')
        #element3.send_keys("hi")

        #this css locater value is for Hide/Show on the practice page
        #element4=driver.find_element_by_css_selector(".inputs.displayed-class")
        #element4.send_keys("hi")

        # this css locater value is for Hide/Show on the practice page
        #element5=driver.find_element_by_css_selector('input[id^="displayed"]')
        #element5.send_keys("hi ra")

        # this css locater value is for Switch To Alert Example on the practice page
        #HOW TO FIND CHILD NODES USING CSS SELECTORS
        #element6=driver.find_element_by_css_selector("fieldset>input#name")
        #element6.send_keys("hi")

ll=Listofelements()
ll.List()