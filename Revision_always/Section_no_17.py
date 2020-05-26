#HOW TO FIND OUT THE BEAUTIFUL XPATHS
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class EffectiveXpath():
    def path(self):
        driver=webdriver.Firefox()
        baseurl='https://learn.letskodeit.com'
        driver.get(baseurl)
        #baseurl1 = 'https://learn.letskodeit.com/'
        #driver.get(baseurl1)
        driver.maximize_window()
        driver.implicitly_wait(10)

        #by using single slash
        driver.find_element(By.XPATH, '//div/div/div/div/div/fieldset/input[@id="name"]')
        #by using double slash
        driver.find_element(By.XPATH, '//div//fieldset/input[@id="name"]')

        #how to build the path for the text of an element with out contains
        driver.find_element(By.XPATH, '//div[@id="block-1754138"]//a[text()= "Enroll now"]')

        #how wto use contains method to build the xpath
        driver.find_element(By.XPATH, '//div[@id="block-1754138"]//a[contains(text(), "Enroll now")]')
        #we can use cotains method for any locater
        driver.find_element(By.XPATH, '//div[@id="block-1754138"]//a[contains(@href, "/sign_up")]')
        #how to use double times contains method
        driver.find_element(By.XPATH,
                            '//div[@id="block-1754138"]//a[contains(@href, "/sign_up") and contains(text(),"Enroll now")]')

        #how to use starts-with method
        driver.find_element(By.XPATH, '//div[@id="block-1754138"]//a[starts-with(@href, "/sign_up") ]')

        #how to use following sibling
        driver.find_element(By.XPATH, '')

        #preceding sibling
        driver.find_element(By.XPATH, '//table[@id="product"]//tbody//tr[2]//preceding-sibling::td[contains(text(),"35")]')
        #following sibling
        driver.find_element(By.XPATH, '//table[@id="product"]//tbody//tr[2]//following-sibling::td[3]')