#BROWSER INTERACTIONS
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class Browser_interactions():
    def interactions(self):
        driver=webdriver.Firefox()
        baseurl='https://learn.letskodeit.com/'
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(10)

        #how to get the title
        print driver.title

        #how to get the current url
        print driver.current_url
        #how to refresh the page
        driver.refresh()
        print "page refreshed for the first time"
        #how to refreshh the page
        driver.get(driver.current_url)
        #how to move to the other url
        driver.get("https://www.google.com/")
        time.sleep(3)
        driver.back()
        print "we came back to the parent url"
        time.sleep(3)
        driver.forward()
        print "we came another url like google"
        print driver.page_source
        driver.close()
b=Browser_interactions()
b.interactions()
'''

#HOW TO CLICK AND TYPE ON A WEB ELEMENT
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class Type_on_element():
    def typing(self):
        driver=webdriver.Firefox()
        baseurl='https://learn.letskodeit.com/p/practice'
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(10)

        driver.find_element(By.ID, "name").send_keys("test")
t=Type_on_element()
t.typing()
'''
#HOW TO FIND OUT THE STATE OF AN ELEMENT
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class State_of_element():
    def state(self):
        driver=webdriver.Firefox()
        baseurl='https://learn.letskodeit.com/p/practice'
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(10)

        switch_alert=driver.find_element(By.ID, "name")
        switch_alert.send_keys("test")
        print ("is enabled?:",switch_alert.is_enabled())

s=State_of_element()
s.state()
'''
#WORKING WITH RADIO BUTTONS
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class Radio_buttons():
    def Radio(self):
        driver=webdriver.Firefox()
        baseurl='https://learn.letskodeit.com/p/practice'
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(10)

        lists=driver.find_elements(By.XPATH, '//input[contains(@name,"cars") and contains(@type,"radio")]')
        print len(lists)

        for radioButton in lists:
            isSelected = radioButton.is_selected()

            if not isSelected:
                radioButton.click()
                time.sleep(2)


r=Radio_buttons()
r.Radio()

'''
#HOW TO WORK WITH CHECK BOXES
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class Radio_buttons():
    def Radio(self):
        driver=webdriver.Firefox()
        baseurl='https://learn.letskodeit.com/p/practice'
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(10)

        lists=driver.find_elements(By.XPATH, '//input[contains(@name,"cars") and contains(@type,"checkbox")]')
        print len(lists)
        for checkbox in lists:
            isSelected = checkbox.is_selected()

            if not isSelected:
                checkbox.click()
                time.sleep(2)


r=Radio_buttons()
r.Radio()
'''

#HOW TO WORK WITH THE DROPDOWN WHICH CONTAINS SELECT INPUT TAG
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
class Dropdown():
    def dropdown(self):
        driver=webdriver.Firefox()
        baseurl='https://learn.letskodeit.com/p/practice'
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(10)

        cars_dropdown=driver.find_element(By.ID, "carselect")
        sel=Select(cars_dropdown)

        sel.select_by_value("benz")
        print "benz got seleted"
        time.sleep(4)
        sel.select_by_visible_text("Honda")
        print "honda got selected"
        time.sleep(4)
        sel.select_by_index(0)
        print "bmw got selected"
        time.sleep(4)

d=Dropdown()
d.dropdown()
'''


#WORKING WITH HIDDEN ELEMENTS
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.select import Select
import time
class Hidden_elements():
    def hidden(self):
        driver=webdriver.Firefox()
        baseurl='https://learn.letskodeit.com/p/practice'
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(10)

        show_button_box=driver.find_element(By.CSS_SELECTOR, '#displayed-text')
        print ("is displayed?:",show_button_box.is_displayed())
        hide=driver.find_element(By.CSS_SELECTOR, '#hide-textbox')
        hide.click()
        print ("is displayed?:",show_button_box.is_displayed())
        time.sleep(4)
        show=driver.find_element(By.CSS_SELECTOR, '#show-textbox')
        show.click()
        print ("is displayed?:", show_button_box.is_displayed())

h=Hidden_elements()
h.hidden()
'''