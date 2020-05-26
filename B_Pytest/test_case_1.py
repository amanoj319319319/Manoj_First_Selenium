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
    a=10
    b=20
    #@pytest.mark.skip()
    #@pytest.mark.skipif(a!=b,reason="This test wants to be run on Linux machine")
    #@pytest.mark.run(order=2)
    def test_Login(self,test_setUp):
        driver.find_element_by_xpath("//*[@id='navbar']/div/div/div/ul/li[2]/a").click()
        time.sleep(10)
        title_page=driver.title
        print (title_page)
        if title_page==driver.title:
            print ("hai test_login method has been executed successfully")
            assert True
        else:
            assert False

    #@pytest.mark.run(order=1)
    def test_practice(self,test_setUp):
        driver.find_element_by_xpath("//*[@id='navbar']/div/div/div/ul/li[1]/a").click()
        time.sleep(10)
        title=driver.title
        print (title)
        print ("hai test_login method has been executed successfully")





