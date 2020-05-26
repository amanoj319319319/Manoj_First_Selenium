'''
from selenium import webdriver
import allure
import pytest
import time
from allure_commons.types import AttachmentType

class Test_Allure_class():
    @pytest.fixture()
    def Test_setUp(self):
        print ("i will be printed every time before executing each tests of Allure_class")
        global driver
        driver=webdriver.Chrome()
        driver.get("https://learn.letskodeit.com")
        time.sleep(3)
        yield
        driver.close()
        driver.quit()

    @allure.severity(allure.severity_level.NORMAL)
    def test_practice(self,Test_setUp):
        #self.driver=webdriver.Chrome()
        #self.driver.get("https://learn.letskodeit.com")
        driver.find_element_by_xpath("//*[@id='navbar']/div/div/div/ul/li[1]/a").click()
        time.sleep(3)
        title_page=driver.title
        print (title_page)
        if title_page == driver.title:
            assert True
            print ("True title of web page is:-",title_page)
            #self.driver.close()
        else:
            #self.driver.close()
            assert False
            print ("Test method failed")

    @allure.severity(allure.severity_level.CRITICAL)
    def test_Login(self,Test_setUp):
        #self.driver=webdriver.Chrome()
        #self.driver.get("https://learn.letskodeit.com")
        driver.find_element_by_xpath("//*[@id='navbar']/div/div/div/ul/li[2]/a").click()
        time.sleep(3)
        title_page=driver.title
        print (title_page)
        if title_page == "Hai":
            assert True
            print ("True title of web page is:-",title_page)
        else:
            allure.attach(driver.get_screenshot_as_png(),name="LoginScreenshot",attachment_type=AttachmentType.PNG)
            #self.driver.close()
            assert False
            print ("Test method failed")

'''





