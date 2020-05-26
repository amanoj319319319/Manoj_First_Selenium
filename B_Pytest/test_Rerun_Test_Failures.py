#the commonds which we use for this rerun failed test cases they might not work with python 2.x version
#they will work in python 3.x versions
'''
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

    #@pytest.mark.flaky(reruns=2)
    @pytest.mark.flaky(reruns=5, reruns_delay=5)
    def test_practice(self,test_setUp):
        driver.find_element_by_xpath("//*[@id='navbar']/div/div/div/ul/li[1]/a").click()
        time.sleep(10)
        title=driver.title
        print (title)
        assert title=="manoj"
        print ("hai test_login method has been executed successfully")
        a=10
        b=20
        print ("The addition of a and b is:-",(a+b))

'''



#https://pypi.org/project/pytest-rerunfailures/   (Refer thsi site carefully)