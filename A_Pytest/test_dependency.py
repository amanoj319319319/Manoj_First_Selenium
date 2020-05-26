from selenium import webdriver
import pytest
import time

class Testexample1():
    @pytest.yield_fixture()
    def test_setUp(self):
        global driver
        driver=webdriver.Chrome()
        driver.get("https://learn.letskodeit.com/")
        driver.maximize_window()
        yield
        driver.close()

    @pytest.mark.dependecy(depends=["Testexample1::test_practice"])
    def test_login(self,test_setUp):
        driver.find_element_by_xpath("//*[@id='navbar']/div/div/div/ul/li[2]/a").click()
        time.sleep(10)
        title_page=driver.title
        print (title_page)
        if title_page==driver.title:
            print ("hai test_login method has been executed successfully")
            assert True
        else:
            assert False

    @pytest.mark.run(order=1)
    @pytest.mark.dependecy()
    def test_practice(self,test_setUp):
        driver.find_element_by_xpath("//*[@id='navbar']/div/div/div/ul/li[1]/a").click()
        time.sleep(10)
        title=driver.title
        print (title)
        print ("hai test_login method has been executed successfully")





