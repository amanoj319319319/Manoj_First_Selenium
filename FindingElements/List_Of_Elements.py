'''
from selenium import webdriver
from selenium.webdriver.common.by import By
class BYDEMO(object):
    def element(self):
        baseurl="https://learn.letskodeit.com/p/practice"
        driver=webdriver.Chrome()
        driver.get(baseurl)

        elementbyCLASSNAME=driver.find_elements(By.CLASS_NAME,"inputs")
        print len(elementbyCLASSNAME)

        if elementbyCLASSNAME is not None:
            print "CLASS_NAME: size of the list is :",len(elementbyCLASSNAME)

        elementbyTAGNAME=driver.find_elements_by_tag_name("td")
        print len(elementbyTAGNAME)

        if elementbyTAGNAME is not None:
            print "TAG NAME: size of the list is:",len(elementbyTAGNAME)

f=BYDEMO()ss
f.element()
'''
#len() built in method wont work for driver.find_element_by_ and find_element(By.)....this type of formats ,
#it wont works
#len() works for the method like find_elements(By.) and find_elements_by_tag_name("td")..it works this method .

'''
from selenium import webdriver
import time
url="https://en-gb.facebook.com/login/"

driver=webdriver.Firefox()
driver.get(url)

username=eval(raw_input("enter your username:"))
password=eval(raw_input("enter your password:"))

element_by_id=driver.find_element_by_id("email")
element_by_ide=driver.find_element_by_id("pass")
element_by_id.send_keys(username)
element_by_ide.send_keys(password)
element_by_idee=driver.find_element_by_id("loginbutton")
element_by_idee.click()
time.sleep(15)
'''