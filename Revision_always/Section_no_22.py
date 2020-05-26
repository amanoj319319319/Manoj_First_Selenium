#SECTION_NO_22
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class switch_window():
    def window(self):
        driver = webdriver.Firefox()
        baseurl = 'https://learn.letskodeit.com/p/practice'
        driver.get(baseurl)
        driver.maximize_window()
        driver.implicitly_wait(10)

        #first we need to find the parent handle number
        parent_handle=driver.current_window_handle
        print parent_handle

        #then , we need to perform an action over the other handle element which is on parent page
        open_window=driver.find_element(By.CSS_SELECTOR, '#openwindow')
        open_window.click()
        time.sleep(5)

        #then, we need to find out the other window handle number aslo
        other_window_handle=driver.window_handles
        #window_handles will brings the both parent and other window handle numbers
        print other_window_handle

        for handle in other_window_handle:
            if handle not in parent_handle:
                driver.switch_to.window(handle)
                time.sleep(10)
                search = driver.find_element(By.ID, 'search-courses')
                search.send_keys("python")
                time.sleep(3)
                driver.close()
                break


        #i want to work with parent handle page elements
        time.sleep(5)
        driver.switch_to.window(parent_handle)
        driver.find_element(By.ID, 'name').send_keys("test")

s=switch_window()
s.window()

'''

#HOW TO WORK WITH FRAMES
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class switch_frame():
    def frame(self):
        driver = webdriver.Firefox()
        baseurl = 'https://learn.letskodeit.com/p/practice'
        driver.get(baseurl)
        driver.maximize_window()
        driver.implicitly_wait(10)

        #working on current frame
        driver.find_element(By.ID, "name").send_keys("test")

        time.sleep(10)
        #switching to other frame
        #if i want to switch to other frames , i have three ways
        #one is using NAME,ID,NUMBERS
        #this is with the help of ID frame
        #driver.switch_to.frame("courses-iframe")
        
    
        # below i used NUMBER
        driver.switch_to.frame(0)
        driver.find_element(By.CSS_SELECTOR, '#search-courses').send_keys("hi")

        time.sleep(10)
        #by using default _content() method i can able to come back to the current frame
        driver.switch_to.default_content()
        driver.find_element(By.ID, "name").send_keys("tasty")

s=switch_frame()
s.frame()
'''

#HOW TO WORK WITH THE ALERTS(JAVA ALERTS) WHICH ARE ON THE PRACTICE PAGE
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class switch_Alert():
    def alert(self):
        driver = webdriver.Firefox()
        baseurl = 'https://learn.letskodeit.com/p/practice'
        driver.get(baseurl)
        driver.maximize_window()
        driver.implicitly_wait(10)

        switch_textbox=driver.find_element(By.ID, "name")
        switch_textbox.send_keys("test")

        Alert=driver.find_element(By.CSS_SELECTOR, '#alertbtn')
        Alert.click()
        time.sleep(2)
        Alert1=driver.switch_to.alert
        Alert1.accept()

        time.sleep(5)
        switch_textbox = driver.find_element(By.ID, "name")
        switch_textbox.send_keys("manoj")

        Confirm=driver.find_element(By.CSS_SELECTOR, '#confirmbtn')
        Confirm.click()
        time.sleep(2)
        Confirm1=driver.switch_to.alert
        Confirm1.dismiss()

s=switch_Alert()
s.alert()
'''







