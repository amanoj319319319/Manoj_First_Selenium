'''
from selenium import webdriver
class Findelement():
    def element(self):
        baseurl="https://en-gb.facebook.com/login/"
        driver=webdriver.Firefox()
        driver.get(baseurl)
        elementbyid=driver.find_element_by_id("isprivate")
        if elementbyid is not None:
            print "we found the id element"
        elementbyclass=driver.find_element_by_name("isprivate")
        if elementbyclass is not None:
            print "we found the class name element"
f=Findelement()
f.element()
'''

from selenium import webdriver
class Findelement():
    def element(self):
        baseurl="https://en-gb.facebook.com/login/"
        driver=webdriver.Firefox()
        driver.get(baseurl)
        elementbyid=driver.find_element_by_id("isprivate")
        if elementbyid is not None:
            print "we found the id element"
        elementbyclass=driver.find_element_by_name("isprivate")
        if elementbyclass is not None:
            print "we found the class name element"
        #the below element id is dynamic type of id ,it will vary every time ,so we shouldnt
        #use this type of dynamic ids and also name="Text"..this is one common for everything
        #right ,,so we should not use name="Text" also.
        elementbyid = driver.find_element_by_class_name("_3_s0 _1toe _3_s1 _3_s1 uiBoxGray noborder" )
        if elementbyid is not None:
            print "we found element id"
f=Findelement()
f.element()


