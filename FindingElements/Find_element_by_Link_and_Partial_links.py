'''
from selenium import webdriver
class Findelement():
    def element(self):
        baseurl="https://learn.letskodeit.com/p/practice"
        driver=webdriver.Firefox()
        driver.get(baseurl)
        elementbyLINK=driver.find_element_by_link_text('Login')
        if elementbyLINK is not None:
            print "we found the LINK TEST element"
        elementbyPARTIALLINK=driver.find_element_by_partial_link_text("Pract")
        if elementbyPARTIALLINK is not None:
            print "we found the PARTIAL LINK TEST element"
f=Findelement()
f.element()
'''
 # hi raw_input()
 # how ar eyou
 # where are yoy
