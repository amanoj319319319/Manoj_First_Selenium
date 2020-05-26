''
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver=webdriver.Firefox()
driver.maximize_window()
baseurl='https://www.google.com/'
driver.implicitly_wait(10)
driver.get(baseurl)

# gmaillink=driver.find_element_by_link_text('Gmail')
# gmaillink.click()

# partialgmail=driver.find_element_by_partial_link_text('Gma')
# partialgmail.click()

time.sleep(5)
driver.quit()
'''
'''

###Calender Selection
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class calender_selection():
    def calender(self):
        driver=webdriver.Firefox()
        driver.maximize_window()
        baseurl='https://www.expedia.com/'
        driver.get(baseurl)
        driver.implicitly_wait(10)

        driver.find_element(By.CSS_SELECTOR,'#tab-flight-tab-hp > span.icons-container').click()

        start=driver.find_element(By.CSS_SELECTOR,'#flight-origin-hp-flight')
        start.send_keys('Hyderabad')

        end=driver.find_element(By.CSS_SELECTOR,'#flight-destination-hp-flight')
        end.send_keys('Pune')

        departindfield=driver.find_element(By.CSS_SELECTOR,'#flight-departing-hp-flight')
        departindfield.click()
        selectiondate=driver.find_element(By.XPATH,'//button[contains(@data-day, "15") and contains(@data-month, "11")]')
        selectiondate.click()

        returningfileld=driver.find_element(By.CSS_SELECTOR,'#flight-returning-hp-flight')
        returningfileld.click()
        returningfileld.clear()
        time.sleep(3)
        returndate=driver.find_element(By.XPATH,'//button[contains(@data-day, "10") and contains(@data-month, "0")]')
        returndate.click()

        search=driver.find_element(By.CSS_SELECTOR,'#gcw-flights-form-hp-flight > div.cols-nested.ab25184-submit > label > button')
        search.click()

cc=calender_selection()
cc.calender()
'''

'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class calender_selection():
    def calender(self):
        driver=webdriver.Firefox()
        driver.maximize_window()
        baseurl='https://www.expedia.com/'
        driver.get(baseurl)
        driver.implicitly_wait(10)

        flights_tab=driver.find_element(By.CSS_SELECTOR,'#tab-flight-tab-hp > span.icons-container')
        flights_tab.click()

        startplace=driver.find_element(By.CSS_SELECTOR,'#flight-origin-hp-flight')
        startplace.send_keys('Hyderabad')

        endplace=driver.find_element(By.CSS_SELECTOR,'#flight-destination-hp-flight')
        endplace.send_keys('Pune')

        departuredate=driver.find_element(By.CSS_SELECTOR,'#flight-departing-hp-flight')
        departuredate.click()

        calendermonth_left=driver.find_elements(By.XPATH, '//div[@id="flight-departing-wrapper-hp-flight"]/div/div/div[2]')
        time.sleep(3)

        for date in calendermonth_left:
            if " 30" in date.text:
                date.click()
                time.sleep(5)
                break
cc=calender_selection()
cc.calender()

'''

'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class autocompleteselection(object):
    def autocomplete(self):
        driver=webdriver.Firefox()
        driver.maximize_window()
        baseurl='https://www.google.com/'
        driver.get(baseurl)
        driver.implicitly_wait(10)

        search_box=driver.find_element(By.CSS_SELECTOR, '#tsf > div:nth-child(2) > div > div.RNNXgb > div > div.a4bIc > input')
        search_box.send_keys('python')
        time.sleep(3)

        itemto_select=driver.find_element(By.CSS_SELECTOR, '#tsf > div:nth-child(2) > div > div.UUbT9 > div.aajZCb > ul > li:nth-child(3) > div.sbtc > div > span')
        itemto_select.click()
        time.sleep(2)


aa=autocompleteselection()
aa.autocomplete()


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class autocompleteselection(object):
    def autocomplete(self):
        driver=webdriver.Firefox()
        driver.maximize_window()
        baseurl='https://www.google.com/'
        driver.get(baseurl)
        driver.implicitly_wait(10)

'''


