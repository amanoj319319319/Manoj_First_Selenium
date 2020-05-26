'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from Revision_section_no_19_second import ExplicitWaitType
import time

class ExplicitWaitDemo2():

    def test(self):
        baseUrl = "http://www.expedia.com"
        driver = webdriver.Firefox()
        driver.implicitly_wait(.5)
        driver.maximize_window()
        wait = ExplicitWaitType(driver)
        driver.get(baseUrl)
        driver.find_element(By.CSS_SELECTOR, "#tab-flight-tab-hp > span.icons-container").click()
        driver.find_element(By.CSS_SELECTOR, "#flight-origin-hp-flight").send_keys("SFO")
        driver.find_element(By.CSS_SELECTOR, "#flight-destination-hp-flight").send_keys("NYC")
        driver.find_element(By.CSS_SELECTOR, "#flight-departing-hp-flight").send_keys("12/24/2018")
        returnDate = driver.find_element(By.CSS_SELECTOR, "#flight-returning-hp-flight")
        returnDate.clear()
        time.sleep(4)
        returnDate.send_keys("12/26/2018")
        driver.find_element(By.CSS_SELECTOR, "#gcw-flights-form-hp-flight > div.cols-nested.ab25184-submit > label > button").click()

        element = wait.waitForElement("stopFilter_stops-0")
        element.click()

        time.sleep(2)
        driver.quit()

ff = ExplicitWaitDemo2()
ff.test()

'''
#it works very very fine ,but net should be good
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from Revision_section_no_19_second import ExplicitWaitType
import time

class ExplicitWaitDemo2():

    def test(self):
        baseUrl = "http://www.expedia.com"
        driver = webdriver.Firefox()
        driver.implicitly_wait(5)
        driver.maximize_window()
        wait = ExplicitWaitType(driver)
        driver.get(baseUrl)
        driver.find_element(By.CSS_SELECTOR, "#tab-flight-tab-hp > span.icons-container").click()
        driver.find_element(By.CSS_SELECTOR, "#flight-origin-hp-flight").send_keys("SFO")
        driver.find_element(By.CSS_SELECTOR, "#flight-destination-hp-flight").send_keys("NYC")

        driver.find_element(By.CSS_SELECTOR, '#flight-departing-hp-flight').click()
        cal_month1=driver.find_element(By.XPATH, '//div[@id="flight-departing-wrapper-hp-flight"]/div/div/div[2]')
        all_dates1=cal_month1.find_elements(By.TAG_NAME, 'button')

        time.sleep(12)

        for date in all_dates1:
            if "26" in date.text:
                date.click()
                break


        return_date=driver.find_element(By.CSS_SELECTOR, '#flight-returning-hp-flight')
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

        search=driver.find_element(By.CSS_SELECTOR, '#gcw-flights-form-hp-flight > div.cols-nested.ab25184-submit > label > button')
        search.click()
        time.sleep(12)
        element = wait.waitForElement("stopFilter_stops-0")
        element.click()

        time.sleep(2)
        driver.quit()

ff = ExplicitWaitDemo2()
ff.test()

'''

'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class acountclass():
    def account(self):
        driver=webdriver.Firefox()
        baseurl='https://www.expedia.com/'
        driver.get(baseurl)
        driver.maximize_window()
        driver.implicitly_wait(10)

        account=driver.find_element(By.CSS_SELECTOR, '#header-account-menu')
        account.click()
        time.sleep(10)
        sighn_in=driver.find_element(By.CSS_SELECTOR, '#account-signin')
        sighn_in.click()
a=acountclass()
a.account()
'''








