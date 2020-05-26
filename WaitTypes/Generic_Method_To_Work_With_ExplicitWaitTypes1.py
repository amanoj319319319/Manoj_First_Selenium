'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from Generic_Method_To_Work_With_ExplicitWaitTypes import Explicitwaittype
import time

class Explicitwaitdemo():
    def test(self):
        driver=webdriver.Firefox()
        driver.implicitly_wait(5)
        driver.maximize_window()
        wait=Explicitwaittype(driver)
        baseurl='https://www.expedia.com'
        driver.get(baseurl)
        driver.find_element(By.XPATH,'//*[@id="tab-flight-tab-hp"]/span[1]').click()
        driver.find_element(By.XPATH,'//*[@id="flight-origin-hp-flight"]').send_keys('Pune')
        driver.find_element(By.XPATH,'//input[@id="flight-destination-hp-flight"]').send_keys('Chennai')
        driver.find_element(By.XPATH,'//input[@id="flight-departing-hp-flight"]').send_keys('12/15/2018')
        returndate=driver.find_element(By.XPATH,'//input[@id="flight-returning-hp-flight"]')
        time.sleep(3)
        returndate.clear()
        time.sleep(3)

        returndate.send_keys('12/30/2018')
        searchbutton=driver.find_element(By.XPATH,'//*[@id="gcw-flights-form-hp-flight"]/div[7]/label')
        searchbutton.click()

        Element=wait.waitForElement('stopFilter_stops-0')
        Element.click()



        time.sleep(3)
        driver.quit()
ee=Explicitwaitdemo()
ee.test()
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from Generic_Method_To_Work_With_ExplicitWaitTypes import Explicitwaittype
import time

class Explicitwaitdemo():
    def test(self):
        driver=webdriver.Firefox()
        driver.implicitly_wait(5)
        driver.maximize_window()
        wait=Explicitwaittype(driver)
        baseurl='https://www.expedia.com'
        driver.get(baseurl)
        driver.find_element(By.XPATH,'//*[@id="tab-flight-tab-hp"]/span[1]').click()
        driver.find_element(By.XPATH,'//*[@id="flight-origin-hp-flight"]').send_keys('Pune')
        driver.find_element(By.XPATH,'//input[@id="flight-destination-hp-flight"]').send_keys('Chennai')
        driver.find_element(By.XPATH,'//input[@id="flight-departing-hp-flight"]').send_keys('12/15/2018')
        returndate=driver.find_element(By.XPATH,'//input[@id="flight-returning-hp-flight"]')
        time.sleep(3)
        returndate.clear()
        time.sleep(3)

        returndate.send_keys('12/30/2018')
        searchbutton=driver.find_element(By.XPATH,'//*[@id="gcw-flights-form-hp-flight"]/div[7]/label')
        searchbutton.click()
        time.sleep(12)
        element1=wait.waitForElement("stopFilter_stops-0")
        element1.click()

        time.sleep(3)
        driver.quit()
ee=Explicitwaitdemo()
ee.test()
