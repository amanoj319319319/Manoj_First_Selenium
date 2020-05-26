'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
class Chrome(object):
    def chr(self):
        driverlocation="C:\\Users\\Manoj\\Desktop\\MANOJ SORT APPLICATIONS\\chromedriver_win32\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverlocation
        driver=webdriver.Chrome(driverlocation)
        driver.get("https://www.flipkart.com/")
        time.sleep(6)
        driver.close()
c=Chrome()
c.chr()
'''

#section_18 , 101
#browser interactions

#section_18 , 102
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class Browser_interactions(object):
    def Browser(self):
        driver=webdriver.Chrome()
        #maximize_window
        driver.maximize_window()
        #getting title
        title=driver.title
        print ("The title of the webpage is : "+title)
        #getting url
        driver.get("https://www.flipkart.com/")
        #getting current_url
        curr_url=driver.current_url
        print ("The current url is:" +curr_url)
        #refreshing the url
        driver.refresh()
        #again refreshing the url
        time.sleep(6)
        driver.get(driver.current_url)
        #opening another url for performing forword method
        driver.get("https://www.amazon.in/")
        #how to come back to the another url
        driver.back()
        #how to go forward
        driver.forward()
        #how to get the page source
        page=driver.page_source
        print ("The page source is:",page)
        #how to close one window
        driver.close()
        #how to quit from all the windows
        driver.quit()

b=Browser_interactions()
b.Browser()

'''

#Section_19 , 103

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class Browser_interactions(object):
    def Browser(self):
        driver=webdriver.Chrome()
        driver.get("https://www.flipkart.com/")
        title=driver.title
        print ("THe title of the webpage is :" + title)
        driver.close()
b=Browser_interactions()
b.Browser()

















