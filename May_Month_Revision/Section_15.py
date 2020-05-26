#What is DOM ... Document Object Model
#DOM consists of headers and classes and divs and so many things .

#How to find an element by ID
'''
from selenium import webdriver
import time
class elementbyID():
    def id(self):
        driver=webdriver.Firefox()
        driver.get("https://learn.letskodeit.com/p/practice")
        time.sleep(5)
        elementbyid=driver.find_element_by_id("name")
        if elementbyid is not None:
            print ("the element has been found successfully")
ee=elementbyID()
ee.id()

'''

#How to find an element by NAME
'''
from selenium import webdriver
import time
class elementbyNAME():
    def name(self):
        driver=webdriver.Firefox()
        driver.get("https://learn.letskodeit.com/p/practice")
        time.sleep(5)
        elementbyid=driver.find_element_by_name("enter-name")
        if elementbyid is not None:
            print ("the element has been found successfully")
ee=elementbyNAME()
ee.name()
'''

#If any multiple elements on the web page shares same id means , we should check with some other ,
#things like tag, text, css locater, xpath
#example yahoo.com


#How to find an element by NAME
'''
from selenium import webdriver
import time
class elementbyNAME():
    def name(self):
        driver=webdriver.Firefox()
        driver.get("https://learn.letskodeit.com/p/practice")
        time.sleep(5)
        elementbyid=driver.find_element_by_xpath('//*[@id="name"]')
        if elementbyid is not None:
            print ("the element has been found successfully by using xpath")

        elementbyid1 = driver.find_element_by_css_selector("#name")
        if elementbyid1 is not None:
            print ("the element has been found successfully by using CSS selector")

ee=elementbyNAME()
ee.name()

'''

#Finding an element by using link and partial link methods.
'''
from selenium import webdriver
import time
class elementbylink_partial():
    def link_partial(self):
        driver=webdriver.Firefox()
        driver.get("https://learn.letskodeit.com")
        time.sleep(5)
        elementbyid=driver.find_element_by_link_text("Login")
        if elementbyid is not None:
            print ("the element has been found successfully by using xpath")

        elementbyid1 = driver.find_element_by_partial_link_text("Prac")
        if elementbyid1 is not None:
            print ("the element has been found successfully by using CSS selector")

ee=elementbylink_partial()
ee.link_partial()

'''


#Finding an element by using Tag name and Class name
'''
from selenium import webdriver
import time
class elementbyCLASSNAME():
    def class_tagname(self):
        driver=webdriver.Firefox()
        driver.get("https://learn.letskodeit.com/p/practice")
        time.sleep(5)
        elementbyclass=driver.find_element_by_class_name("displayed-class")
        elementbyclass.send_keys("Hello manoj")
        time.sleep(2)

        if elementbyclass is not None:
            print ("the element has been found successfully by using class_name")

        elementbytag = driver.find_element_by_tag_name("legend")
        text=elementbytag.text

        if elementbytag is not None:
            print ("the element has been found successfully by tag name and text on element is:",text)

ee=elementbyCLASSNAME()
ee.class_tagname()

'''


#Finding elements by using BY class
'''
from selenium import webdriver
from selenium.webdriver.common.by import By

import time
class elementbyid():
    def id(self):
        driver=webdriver.Firefox()
        driver.get("https://learn.letskodeit.com/p/practice")
        time.sleep(5)
        elementbyid=driver.find_element(By.ID,"displayed-text")
        if elementbyid is not None:
            print ("the element has been found successfully by using id")

        
ee=elementbyid()
ee.id()

'''

#Suppose if multiple elements sharing same class or same tag name , how to find out the list ,
#of multiple elements

'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class elementbyid():
    def id(self):
        driver = webdriver.Firefox()
        driver.get("https://learn.letskodeit.com/p/practice")
        time.sleep(5)

        elementbyid = driver.find_elements(By.ID, "displayed-text")
        length1=len(elementbyid)
        if elementbyid is not None:
            print ("the element has been found successfully by using id:"+str(length1))

        elementby_classname=driver.find_elements_by_class_name("inputs")
        length2=len(elementby_classname)
        if elementby_classname is not None:
            print ("The element has been found successfully by using class name:"+str(length2))


ee = elementbyid()
ee.id()

'''