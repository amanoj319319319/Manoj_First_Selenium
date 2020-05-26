from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

class Explicitwaitdemo(object):
    def test(self):
        driver=webdriver.Firefox()
        driver.maximize_window()
        baseurl='https://www.expedia.com'
        driver.get(baseurl)
        driver.find_element(By.XPATH,'//*[@id="tab-flight-tab-hp"]/span[1]').click()
        driver.find_element(By.XPATH,'//input[@id="flight-origin-hp-flight"]').send_keys('Pune')
        driver.find_element(By.XPATH,'//input[@id="flight-destination-hp-flight"]').send_keys('Chennai')
        driver.find_element(By.XPATH,'//input[@id="flight-departing-hp-flight"]').send_keys('12/15/2018')
        returndate=driver.find_element(By.XPATH,'//input[@id="flight-returning-hp-flight"]')
        time.sleep(3)
        returndate.clear()

        returndate.send_keys('12/30/2018')
        searchbutton=driver.find_element(By.XPATH,'//*[@id="gcw-flights-form-hp-flight"]/div[7]/label')
        searchbutton.click()

        wait=WebDriverWait(driver,20,poll_frequency=10,ignored_exceptions=[NoSuchElementException,
                                                                          ElementNotVisibleException,
                                                                          ElementNotSelectableException])
        element=wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='stopFilter_stops-0']")))
        element.click()

        time.sleep(5)
        driver.quit()


e=Explicitwaitdemo()
e.test()
