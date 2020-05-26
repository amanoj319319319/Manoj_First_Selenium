#this tutorial tells us about ho wto work with the elements list ,
#what it means , if the same family (like radio buttons,check boxes,etx),
# group of elements are sharing the some of the same attributes ,then how to do work with that.
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class WorkingWithElementsList():

    def testListOfElements(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        radioButtonsList = driver.find_elements(
            By.XPATH, "//input[contains(@type,'radio') and contains(@name,'cars')]")
        size = len(radioButtonsList)
        print("Size of the list: " + str(size))

        for radioButton in radioButtonsList:
            isSelected = radioButton.is_selected()

            if not isSelected:
                radioButton.click()
                time.sleep(2)

ff = WorkingWithElementsList()
ff.testListOfElements()