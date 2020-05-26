#how to find the calender on the web page
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class calender_finding():
    def calender(self):
        driver=webdriver.Firefox()
        baseurl='https://www.expedia.com/'
        driver.get(baseurl)
        driver.maximize_window()
        driver.implicitly_wait(10)

        flight_tab=driver.find_element(By.CSS_SELECTOR, '#tab-flight-tab-hp > span.icons-container')
        flight_tab.click()

        driver.find_element(By.CSS_SELECTOR, '#flight-departing-hp-flight').click()
        cal_month1 = driver.find_element(By.XPATH, '//div[@id="flight-departing-wrapper-hp-flight"]/div/div/div[2]')
        all_dates1 = cal_month1.find_elements(By.TAG_NAME, 'button')

        time.sleep(12)

        for date in all_dates1:
            if "26" in date.text:
                date.click()
                break

        return_date = driver.find_element(By.CSS_SELECTOR, '#flight-returning-hp-flight')
        return_date.click()
        return_date.clear()
        time.sleep(4)
        cal_month1 = driver.find_element(By.XPATH, '//*[@id="flight-returning-wrapper-hp-flight"]/div/div/div[2]')
        all_dates1 = cal_month1.find_elements(By.TAG_NAME, 'button')

        time.sleep(10)

        for date in all_dates1:
            if "30" in date.text:
                date.click()
                break


cc=calender_finding()
cc.calender()

'''

#Auto complete testing lecture
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Autocomplete():
    def auto(self):
        driver = webdriver.Firefox()
        baseurl = 'https://www.google.com/'
        driver.get(baseurl)
        driver.maximize_window()
        driver.implicitly_wait(10)

        Google_searchbox=driver.find_element(By.CSS_SELECTOR,
                                             '#tsf > div:nth-child(2) > div > div.RNNXgb > div > div.a4bIc > input')
        Google_searchbox.send_keys("python")
        time.sleep(5)
        Python_related=driver.find_element(By.CSS_SELECTOR,
                                           '#tsf > div:nth-child(2) > div > div.UUbT9 > div.aajZCb > ul > li:nth-child(3) > div.sbtc > div > span > b')

        Python_related.click()

aa=Autocomplete()
aa.auto()

'''

#how to take screen shots when we get an error at particular place of element
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Screenshots():
    def screen(self):
        driver = webdriver.Firefox()
        baseurl = 'https://learn.letskodeit.com/p/practice'
        driver.get(baseurl)
        driver.maximize_window()
        driver.implicitly_wait(10)

        Login_link=driver.find_element(By.CSS_SELECTOR, '#navbar > div > div > div > ul > li:nth-child(2) > a')
        Login_link.click()

        time.sleep(10)
        Username=driver.find_element(By.ID, "user_email")
        Username.send_keys('manoj')
        time.sleep(10)
        Password=driver.find_element(By.ID, "user_password")
        Password.send_keys('125')

        Commit=driver.find_element(By.CSS_SELECTOR, '#new_user > div.form-group.text-center > input')
        Commit.click()

        destination_place='C:\\Users\\Manoj\\Desktop\\commit.png'
        try:
            screenshot=driver.save_screenshot(destination_place)
            print ("the scree shot saved to::",destination_place)
        except Exception as e:
            print ("sorry ..screen shot didnt save to the destination place")

s=Screenshots()
s.screen()

'''

#how to create generic path for taking the screenshots
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Screenshots():
    def screen(self):
        driver = webdriver.Firefox()
        baseurl = 'https://learn.letskodeit.com/p/practice'
        driver.get(baseurl)
        driver.maximize_window()
        driver.implicitly_wait(10)

        Login_link=driver.find_element(By.CSS_SELECTOR, '#navbar > div > div > div > ul > li:nth-child(2) > a')
        Login_link.click()

        time.sleep(10)
        Username=driver.find_element(By.ID, "user_email")
        Username.send_keys('manoj')
        time.sleep(10)
        Password=driver.find_element(By.ID, "user_password")
        Password.send_keys('125')

        Commit=driver.find_element(By.CSS_SELECTOR, '#new_user > div.form-group.text-center > input')
        Commit.click()
        self.takescreenshot(driver)

    def takescreenshot(self, driver):
        ''it takes scren shots with diff file numbers''
        filename=str(round(time.time()*1000))+".png"
        destinationfile='C:\\Users\\Manoj\\Desktop\\'+filename

        try:
           driver.save_screenshot(destinationfile)
           print ("the screen shot is saved to :",destinationfile)
        except Exception as e:
           print ("sorry ..screen shot didnt saved to destination file")

s=Screenshots()
s.screen()
'''

#Executing the java script
#Note:- if you get an error like Non object has send_keys ,you can increase the wait time
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class JavaScript():
    def java(self):
        driver=webdriver.Firefox()
        baseurl='https://learn.letskodeit.com/p/practice'
        driver.execute_script("window.location='https://learn.letskodeit.com/p/practice';")
        driver.maximize_window()
        driver.implicitly_wait(10)
        time.sleep(15)
        element=driver.execute_script("return document.getElementById('name');")
        element.send_keys("test")

j=JavaScript()
j.java()
'''


#How to find out the size of the window
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class size_of_window():
    def size(self):
        driver=webdriver.Firefox()
        baseurl='https://learn.letskodeit.com/p/practice'
        driver.execute_script("window.location='https://learn.letskodeit.com/p/practice';")
        driver.maximize_window()
        driver.implicitly_wait(10)

        height=driver.execute_script("return window.innerHeight;")
        width=driver.execute_script("return window.innerWidth;")

        print ("height of the window is :",height)
        print ("width of the window is :",width)

s=size_of_window()
s.size()

'''

#how to scroll an element to view

'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Scroll_element():
    def scroll(self):
        driver = webdriver.Firefox()
        baseurl = 'https://learn.letskodeit.com/p/practice'
        driver.execute_script("window.location='https://learn.letskodeit.com/p/practice';")
        driver.maximize_window()
        driver.implicitly_wait(10)

        #scroll down
        driver.execute_script("window.scrollBy(0,900);")
        time.sleep(3)

        #scroll up
        driver.execute_script("window.scrollBy(0,-300);")

        #finding an element
        driver.find_element(By.CSS_SELECTOR, '#displayed-text').send_keys("test")

s=Scroll_element()
s.scroll()
'''

























