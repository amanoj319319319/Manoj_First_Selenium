#Note:- During this process , when we are providing the executable path , you need to give ,
#\\ and at last you should give geckodriver.exe .(exe - means extension of geckodriver file)
#Running test on firefox browser

'''
from selenium import webdriver
import time
driver=webdriver.Firefox(executable_path="C:\\Users\\Manoj\\Desktop\\MANOJ SORT APPLICATIONS\\geckodriver-v0.23.0-win64\\geckodriver.exe")
driver.get("https://www.flipkart.com")
time.sleep(5)
driver.close()
'''

#using the same code by using class concepts
'''
from selenium import webdriver
import time
class firefoxtest(object):
    def firefox(self):
        driver = webdriver.Firefox(
            executable_path="C:\\Users\\Manoj\\Desktop\\MANOJ SORT APPLICATIONS\\geckodriver-v0.23.0-win64\\geckodriver.exe")
        driver.get("https://www.flipkart.com")
        time.sleep(5)
        driver.close()
ff=firefoxtest()
ff.firefox()
'''

#Doing tests on google chrome using class concepts.

'''
from selenium import webdriver
import os
import time

class chrometests(object):
    def chrome(self):
        driverlocation=("C:\\Users\\Manoj\\Desktop\\MANOJ SORT APPLICATIONS\\chromedriver_win32\\chromedriver.exe")
        os.environ["webdriver.chrome.driver"] = driverlocation
        driver=webdriver.Chrome(driverlocation)
        driver.get("https://www.flipkart.com")
        time.sleep(5)
        driver.close()
cc=chrometests()
cc.chrome()
'''


#Running tests on IE browser
#To run tests on IE browser first we need to set Zoom level as 100 % ,then click on internet -
#options - disable all the four zones which are appearing

'''
from selenium import webdriver
import os
import time

class ietests(object):
    def ie(self):
        driverlocation=("C:\\Users\\Manoj\\Desktop\\MANOJ SORT APPLICATIONS\\IEDriverServer_x64_3.14.0\\IEDriverServer.exe")
        os.environ["webdriver.ie.driver"] = driverlocation
        driver=webdriver.Ie(driverlocation)
        driver.get("https://www.flipkart.com")
        time.sleep(5)
        driver.close()
ii=ietests()
ii.ie()
'''









from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class elementbyid():
    def id(self):
        driver = webdriver.Firefox()
        driver.get("https://learn.letskodeit.com/p/practice")
        time.sleep(5)

        elementbyid = driver.find_elements(By.NAME, "show-hide")
        length1=len(elementbyid)
        if elementbyid is not None:
            print ("the element has been found successfully by using id:"+str(length1))

        elementby_classname=driver.find_elements_by_class_name("inputs")
        length2=len(elementby_classname)
        if elementby_classname is not None:
            print ("The element has been found successfully by using class name:"+str(length2))


ee = elementbyid()
ee.id()











