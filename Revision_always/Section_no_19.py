#HOW TO GET THE TEXT OF AN ELEMENT
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class Text():
    def text(self):
        driver=webdriver.Firefox()
        baseurl='https://learn.letskodeit.com/p/practice'
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(10)

        Login_link=driver.find_element(By.CSS_SELECTOR, '#navbar > div > div > div > ul > li:nth-child(2) > a')
        print Login_link.text
t=Text()
t.text()
'''

#HOW TO GET THE VALUE OF AN ATTRIBUTE
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class Value():
    def value(self):
        driver=webdriver.Firefox()
        baseurl='https://learn.letskodeit.com/p/practice'
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(10)

        #here i am finding the value of an attribute like name which is in switch_alert button
        switch_alert=driver.find_element(By.ID, 'name')
        print switch_alert.get_attribute("name")

v=Value()
v.value()

'''
#HOW TO BUILD THE DYNAMIC PATH IT MEANS BY USING .FORMAT() METHOD
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class Dynamnamic_path():
    def dynamic(self):
        driver=webdriver.Firefox()
        baseurl='https://learn.letskodeit.com/'
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(10)


        enroll_now='//a[contains(@href, "/sign_up") and contains(text(), "{0}")]'
        enroll_now1=enroll_now.format("Enroll now")
        time.sleep(10)
        enroll_now2=driver.find_element(By.XPATH, enroll_now1)
        enroll_now2.click()

d=Dynamnamic_path()
d.dynamic()
'''





