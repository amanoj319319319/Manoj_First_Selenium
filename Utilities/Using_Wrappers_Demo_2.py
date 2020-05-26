#we took (switch to alert example) web element for testing which is there in our practice page
from selenium import webdriver
from selenium.webdriver.common.by import By
from Utilities.Handy_Wrappers import HandyWrappers
#we imported HandyWrappers() class from the Section_19(package).Hnady_Wrappers(module)
import time

class Usingwrappers():
    def test(self):
        baseurl="https://learn.letskodeit.com/p/practice"
        driver=webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(10)
        #we are creating an obj(hw) ref to HandyWrappers() and we passed argument to this class,
        #like driver
        hw=HandyWrappers(driver)
        driver.get(baseurl)

        elememtresult1=hw.iselementpresent(By.ID,"name")
        print str(elememtresult1)

        elememtresult2=hw.elementpresence(By.XPATH,"//input[@id='name']")
        print str(elememtresult2)

        #here ,we gave wrong path as argument to this below method,
        #so that , it produces a booleen value like False
        elememtresult3 = hw.elementpresence(By.XPATH, "//input[@id='nam']")
        print str(elememtresult3)
        time.sleep(3)

        driver.quit()

uu=Usingwrappers()
uu.test()