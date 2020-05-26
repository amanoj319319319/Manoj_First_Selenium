import sys
sys.path.append('C:\Users\Manoj\Desktop\hi')

from selenium import webdriver
from selenium.webdriver.common.by import By
from generic_method_2 import ExplicitWaitType
import time

class ExplicitWaitDemo2():

    def test(self):
        baseUrl = "http://www.expedia.com"
        driver = webdriver.Firefox()
        driver.implicitly_wait(5)
        driver.maximize_window()
        wait = ExplicitWaitType(driver)
        driver.get(baseUrl)
        driver.find_element(By.CSS_SELECTOR, "#tab-flight-tab-hp").click()
        driver.find_element(By.XPATH, '//input[@id="flight-origin-hp-flight"]').send_keys("Hyderabad")
        driver.find_element(By.XPATH, '//input[@id="flight-destination-hp-flight"]').send_keys("Chennai")
        driver.find_element(By.XPATH, '//input[@id="flight-departing-hp-flight"]').send_keys("12/24/2018")
        returnDate = driver.find_element(By.XPATH, '//input[@id="flight-returning-hp-flight"]')
        time.sleep(3)
        returnDate.clear()
        time.sleep(3)
        returnDate.send_keys("12/26/2018")
        driver.find_element(By.XPATH, '//*[@id="gcw-flights-form-hp-flight"]/div[7]/label/button').click()
        time.sleep(5)
        element = wait.waitForElement("stopFilter_stops-0")
        element.click()

        time.sleep(2)
        driver.quit()

ff = ExplicitWaitDemo2()
ff.test()
