#from selenium import webdriver
#import time
#import os
#on Firefox browser
'''
#initiate(set to the value or put in the condition appropriate to the start of an operation) the driver instance 
driver=webdriver.Firefox(executable_path=
                         "C:\\Users\\Manoj\\Desktop\\MANOJ SORT APPLICATIONS\\geckodriver-v0.23.0-win64\\geckodriver.exe")
driver.get("https://learn.letskodeit.com/p/practice")
time.sleep(10)
'''

#On Chrome browser
'''
driver_location="C:\\Users\\Manoj\\Desktop\\MANOJ SORT APPLICATIONS\\chromedriver_win32\\chromedriver.exe"
os.environ["webdriver.chrome.driver"]=driver_location
driver=webdriver.Chrome(driver_location)
driver.get("https://learn.letskodeit.com/p/practice")
time.sleep(5)
'''

#On IE browser
'''
driver_location="C:\\Users\\Manoj\\Desktop\\MANOJ SORT APPLICATIONS\\IEDriverServer_x64_3.14.0\\IEDriverServer.exe"
os.environ["webdriver.ie.driver"]=driver_location
driver=webdriver.Ie(driver_location)
driver.get("https://learn.letskodeit.com/p/practice")
time.sleep(5)
'''

'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class Test(object):
    def tap(self):
        driver=webdriver.Chrome()
        driver.get("https://learn.letskodeit.com/p/practice")
        find_element_byID=driver.find_element(By.ID,"name")
        find_element_byID.send_keys("hai")
        time.sleep(5)
t=Test()
t.tap()
'''

'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class Test(object):
    def tap(self):
        driver=webdriver.Chrome()
        driver.get("https://learn.letskodeit.com/p/practice")
        time.sleep(5)
        element_tag=driver.find_elements_by_id("name")
        a=len(element_tag)
        print ("list of elements presented with name is",str(a))
t=Test()
t.tap()
'''


from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class Test(object):
    def tap(self):
        driver=webdriver.Chrome()
        driver.get("https://learn.letskodeit.com/p/practice")
        time.sleep(5)
        elementbyID=driver.find_element(By.TAG_NAME,"h1")
        print ("The text of the element is:-",elementbyID.text)
t=Test()
t.tap()
























