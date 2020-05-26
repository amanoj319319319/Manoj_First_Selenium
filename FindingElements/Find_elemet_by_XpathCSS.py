'''
from selenium import webdriver
class Findelement():
    def element(self):
        baseurl="https://en-gb.facebook.com/login/"
        driver=webdriver.Firefox()
        driver.get(baseurl)
        elementbyXPATH=driver.find_element_by_xpath('//*[@id="globalContainer"]')
        if elementbyXPATH is not None:
            print "we found the XPATH element"
        elementbyCSSSELECTOR=driver.find_element_by_css_selector("#globalContainer")
        if elementbyCSSSELECTOR is not None:
            print "we found the CSS SELECTOR element"
f=Findelement()
f.element()
'''