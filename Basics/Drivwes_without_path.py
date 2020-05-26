'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import sys
class mozilla():
    def test(self):
        driver=webdriver.Firefox(executable_path='C:\\Users\\Manoj\\Desktop\\MANOJ SORT APPLICATIONS\\geckodriver.exe')
        baseurl='https://www.google.com/'
        driver.get(baseurl)
        driver.implicitly_wait(10)
        driver.maximize_window()

mm=mozilla()
mm.test()

'''

'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
class chrome():
    def test(self):
        driverlocation='C:\\Users\\Manoj\\Desktop\\MANOJ SORT APPLICATIONS\\chromedriver.exe'
        os.environ['webdriver.chrome.driver']=driverlocation
        driver=webdriver.Chrome()
        driver.get('https://www.google.com/')
        driver.maximize_window()
        driver.implicitly_wait(10)

cc=chrome()
cc.test()
'''

'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
class iedriever():
    def test(self):
        driverlocation='C:\\Users\\Manoj\\Desktop\\MANOJ SORT APPLICATIONS\\IEDriverServer.exe'
        os.environ['webdriver.IE.driver']=driverlocation
        driver=webdriver.Ie()
        driver.get('https://www.google.com/')
        driver.maximize_window()
        driver.implicitly_wait(10)

cc=iedriever()
cc.test()
'''

#how to find out the List of the Elements
#we can find out list of elements only by using find_elements() and find_elements_by_locatername() methods only
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

        elementbytag=driver.find_elements_by_tag_name('input')
        list1=len(elementbytag)

        if elementbytag is not None:
            print ("elements are found and length of elementbytag is:"+str(list1))

        elementbyclass=driver.find_elements(By.CLASS_NAME, 'inputs')
        list2=len(elementbyclass)

        if elementbyclass is not None:
            print ("elements are found and the list of elementbyclass is:")+str(list2)

ll=Listofelements()
ll.List()

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