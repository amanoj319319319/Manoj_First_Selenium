#SECTION_NUMBER_IN_UDEMY=21#

#CALENDER TASK
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


class Calender():
    def cal(self):
        driver=webdriver.Firefox()
        baseurl='https://www.expedia.com/'
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(10)

        time.sleep(6)
        flights_tab=driver.find_element(By.CSS_SELECTOR, '#tab-flight-tab-hp > span.icons-container')
        flights_tab.click()

        from_area=driver.find_element(By.CSS_SELECTOR, '#flight-origin-hp-flight')
        from_area.send_keys('Chennai, India (MAA-Chennai Intl.)')

        to_area=driver.find_element(By.CSS_SELECTOR, '#flight-destination-hp-flight')
        to_area.send_keys('Pune, India (PNQ-Lohegaon)')

        departure_date=driver.find_element(By.CSS_SELECTOR, '#flight-departing-hp-flight')
        departure_date.click()
        cal_month=driver.find_element(By.CSS_SELECTOR, '#flight-departing-wrapper-hp-flight > div > div > div:nth-child(4)')
        dep_date=cal_month.find_elements(By.TAG_NAME, 'button')
        for date in dep_date:
            if "20" in date.text:
                date.click()
                time.sleep(10)
                break

        return_date = driver.find_element(By.CSS_SELECTOR, '#flight-returning-hp-flight')
        return_date.click()
        return_date.clear()
        time.sleep(6)
        cal_month1 = driver.find_element(By.CSS_SELECTOR,
                                        '#flight-returning-wrapper-hp-flight > div > div > div:nth-child(4)')
        ret_date = cal_month1.find_elements(By.TAG_NAME, 'button')
        for date in ret_date:
            if "30" in date.text:
                date.click()
                time.sleep(10)
                break

        search_button=driver.find_element(By.CSS_SELECTOR, '#gcw-flights-form-hp-flight > div.cols-nested.ab25184-submit > label > button')
        search_button.click()

        Nonstop_checkbox = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.ID, "stopFilter_stops-0")))
        Nonstop_checkbox.click()


c=Calender()
c.cal()
'''

#AUTO COMPLETE TASK
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Autocomplete():
    def auto(self):
        driver=webdriver.Firefox()
        baseurl='https://www.google.com/'
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(10)

        google_search=driver.find_element(By.CSS_SELECTOR, '#tsf > div:nth-child(2) > div > div.RNNXgb > div > div.a4bIc > input')
        google_search.send_keys('python')

        time.sleep(4)
        selecting_auto_dropdown=driver.find_element(By.XPATH, '//*[@id="tsf"]/div[2]/div/div[2]/div[2]/ul/li[3]/div[1]/div/span/b')
        selecting_auto_dropdown.click()

a=Autocomplete()
a.auto()
'''

#SCREEN SHOT TASK..BOTH INDIVIDUAL AND GENERIC METHODS
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Screenshot():
    def screen(self):
        driver=webdriver.Firefox()
        baseurl='https://learn.letskodeit.com/p/practice'
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(10)

        login_link=driver.find_element(By.CSS_SELECTOR, '#navbar > div > div > div > ul > li:nth-child(2) > a')
        login_link.click()

        time.sleep(6)

        user_name=driver.find_element(By.CSS_SELECTOR, '#user_email')
        user_name.send_keys('manoj')

        password=driver.find_element(By.CSS_SELECTOR, '#user_password')
        password.send_keys('987')

        commit=driver.find_element(By.NAME, 'commit')
        commit.click()
        time.sleep(6)
        #this is for individual element
        #file_save_location='C:\\Users\\Manoj\\Desktop\\commiting.png'
        #screen=driver.save_screenshot(file_save_location)
        #print "your screen shot has been saved to the location"
        self.screenshot(driver)

    def screenshot(self,driver):
        file_name=str(round(time.time() *1000))+'.png'
        file_save_location='C:\\Users\\Manoj\\Desktop\\'+file_name
        driver.save_screenshot(file_save_location)
        print "your screen shot has been saved"


s=Screenshot()
s.screen()

'''

#EXECUTING JAVA SCRIPTS
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Javascript():
    def java(self):
        driver=webdriver.Firefox()
        #baseurl='https://learn.letskodeit.com/p/practice'
        driver.execute_script("window.location='https://learn.letskodeit.com/p/practice';")
        driver.maximize_window()
        #driver.get(baseurl)
        driver.implicitly_wait(10)

        time.sleep(15)
        switch_element=driver.execute_script("return document.getElementById('name');")
        switch_element.send_keys("test")

j=Javascript()
j.java()
'''
#HOW TO FIND OUT THE SIZE OF THE WINDOW
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Size_window():
    def window(self):
        driver=webdriver.Firefox()
        #baseurl='https://learn.letskodeit.com/p/practice'
        driver.execute_script("window.location='https://learn.letskodeit.com/p/practice';")
        driver.maximize_window()
        #driver.get(baseurl)
        driver.implicitly_wait(10)

        height=driver.execute_script("return window.innerHeight")
        width=driver.execute_script("return window.innerWidth")
        print ("heoght of the window is",height)
        print ("width of the window is",width)

s=Size_window()
s.window()
'''
#HOW DO YOU SCROLL AN ELEMENT ON THE WEB PAGE TO VIEW
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Scrolling_element():
    def scroll(self):
        driver=webdriver.Firefox()
        #baseurl='https://learn.letskodeit.com/p/practice'
        driver.execute_script("window.location='https://learn.letskodeit.com/p/practice';")
        driver.maximize_window()
        #driver.get(baseurl)
        driver.implicitly_wait(10)

        time.sleep(5)
        driver.execute_script("window.scrollBy(0,900);")
        print ("the web page has been scrolled down")
        time.sleep(10)

        driver.execute_script("window.scrollBy(0,-900);")
        print ("the web page has been scroled up")

s=Scrolling_element()
s.scroll()
'''