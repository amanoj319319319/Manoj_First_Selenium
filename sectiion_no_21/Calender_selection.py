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


#it is working fine
#no need to reffer the above code which i have written
#in this code , we have written generic path for the calender selection
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class CalendarSelection():

    def test1(self):
        baseUrl = "http://www.expedia.com"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        # Click flights tab
        driver.find_element_by_id("tab-flight-tab").click()
        # Find departing field
        departingField = driver.find_element_by_id("flight-departing")
        # Click departing field
        departingField.click()
        # Find the date to be selected
        # Expedia website has changed the DOM after the lecture was made
        # Updated new xpath
        dateToSelect = driver.find_element(By.XPATH,
                                           "(//div[@class='datepicker-cal-month'])[1]//button[text()='30']")
        # Click the date
        dateToSelect.click()

        time.sleep(3)
        driver.quit()

    def test2(self):
        baseUrl = "http://www.expedia.com"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        # Click flights tab
        driver.find_element_by_id("tab-flight-tab-hp").click()
        # Click departing field
        driver.find_element_by_id("flight-departing-hp-flight").click()
        # Expedia website has changed the DOM after the lecture was made
        # Updated new xpath
        calMonth = driver.find_element(By.XPATH, '//div[@id="flight-departing-wrapper-hp-flight"]/div/div/div[2]')
        allValidDates = calMonth.find_elements(By.TAG_NAME, "button")

        time.sleep(12)

        for date in allValidDates:
            if "30" in date.text:
                date.click()
                break

ff = CalendarSelection()
ff.test2()

'''