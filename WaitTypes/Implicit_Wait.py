'''
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
'''
class Implicitwait(object):
    def test(self):
        driver=webdriver.Firefox()
        baseurl='https://www.facebook.com/'
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(10)

        emaillink=driver.find_element(By.XPATH,"//input[@id='email']")
        emaillink.send_keys("a.manoj16@gmail.com")

        password=driver.find_element(By.XPATH,"//input[@id='pass']")
        password.send_keys('santhuji')
i=Implicitwait()
i.test()


class google(object):
    def test(self):
        baseurl='https://www.google.com/'
        driver=webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(10)
        google1=driver.find_element(By.XPATH,'//input[@title="Search"]')
        google1.send_keys('facebook login')
        google1.submit()

        link1=driver.find_element(By.XPATH,'//*[@id="rso"]/div[1]/div/div[2]/div/div/div[1]/a/h3')
        link1.click()

        email=driver.find_element(By.ID,'email')
        email.send_keys('a.manoj16@gmail.com')

        password=driver.find_element(By.ID,'pass')
        password.send_keys('santhuji')

        loginlink=driver.find_element(By.XPATH,'//input[@id="u_0_2"]')
        loginlink.click()

g=google()
g.test()
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from Generic_Method_To_Work_With_ExplicitWaitTypes import Explicitwaittype
import time

class Explicitwaitdemo():
    def test(self):
        driver=webdriver.Firefox()
        #driver.implicitly_wait(5)
        driver.maximize_window()
        wait=Explicitwaittype(driver)
        baseurl='https://www.expedia.com'
        driver.get(baseurl)
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, '//*[@id="tab-flight-tab-hp"]/span[1]/span').click()
        driver.find_element(By.XPATH, '//input[@id="flight-origin-hp-flight"]').send_keys('Pune')
        driver.find_element(By.XPATH, '//input[@id="flight-destination-hp-flight"]').send_keys('Chennai')
        driver.find_element(By.XPATH, '//input[@id="flight-departing-hp-flight"]').send_keys('12/15/2018')
        returndate=driver.find_element(By.XPATH, '//input[@id="flight-returning-hp-flight"]')
        time.sleep(3)
        returndate.clear()
        time.sleep(3)

        returndate.send_keys('12/30/2018')
        searchbutton=driver.find_element(By.XPATH, '//*[@id="gcw-flights-form-hp-flight"]/div[7]/label')
        searchbutton.click()

        Element=wait.waitForElement('stopFilter_stops-0')
        time.sleep(15)
        Element.click()



        time.sleep(3)
        driver.quit()
ee=Explicitwaitdemo()
ee.test()
