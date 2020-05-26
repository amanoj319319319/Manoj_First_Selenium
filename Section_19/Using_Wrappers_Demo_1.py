##we took switch to (alert example web element) for testing which is there in our practice page
from selenium import webdriver
from selenium.webdriver.common.by import By
from Section_19.Hnady_Wrappers import HandyWrappers
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
        #we are calling getelement() metghod from HandyWrappers() class with help of obj ref var,
        #like hw
        #we passed an argument(locater="name") to this below method which came from HandyWrappers class
        textfield1=hw.getelement("name")
        textfield1.send_keys('text')
        time.sleep(2)
        #here we called getelement()method again ,and we did give another argument like "xpath"
        textfield2=hw.getelement('//input[@id="name"]',locatertype='xpath')
        #when we use this clear method ,it will erace the send_keys input from the text box.
        textfield2.clear()

        

uu=Usingwrappers()
uu.test()

