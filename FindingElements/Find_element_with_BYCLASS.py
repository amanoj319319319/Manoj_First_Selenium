'''
from selenium import webdriver
from selenium.webdriver.common.by import By
class BYDEMO():
    def element(self):
        baseurl="https://learn.letskodeit.com/p/practice"
        driver=webdriver.Firefox()
        driver.get(baseurl)
        elementbyID=driver.find_element(By.ID,"name")

        if elementbyID is not None:
            print "we found the ID element"
        elementbyLINKTEXT=driver.find_element(By.LINK_TEXT,"Login")

        if elementbyLINKTEXT is not None:
            print "we found the TAG NAME element:"
        elementbyXPATH=driver.find_element(By.XPATH,'//*[@id="name"]')

        if elementbyXPATH is not None:
            print "we found the XAPTH element"

f=BYDEMO()
f.element()
'''