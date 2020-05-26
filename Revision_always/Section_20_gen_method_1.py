from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class HandyWrappers():

    def __init__(self, driver):
        self.driver = driver

    def getByType(self, locatorType):
        locatorType=locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return  By.CSS_SELECTOR
        else:
            print "we did not find the locate type"
        return False

    def getElement(self, locator, locatorType="id"):
        element=None
        try:
            bytype=self.getByType(locatorType)
            element=self.driver.find_element(bytype, locator)
            print "element found"
        except Exception as e:
            print "element not found"
        return element
