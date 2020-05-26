'''
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
import time


@pytest.fixture(scope="class")
def setup(request):
    print("initiating chrome driver")
    driver = webdriver.Chrome()
    request.cls.driver = driver
    driver.get("http://seleniumeasy.com/test")
    driver.maximize_window()

    yield driver
    driver.close()


@pytest.mark.usefixtures("setup")
class TestExample:

    @pytest.mark.smoke
    def test_title(self):
        print("Verify title...")
        assert "Selenium Easy" in self.driver.title

    @pytest.mark.smoke
    def test_content_text (self):
        print("Verify content on the page...")
        centertext = self.driver.find_element_by_css_selector('.tab-content .text-center').text
        assert "WELCOME TO SELENIUM EASY DEMO" == centertext

    @pytest.mark.regression
    @pytest.mark.smoke
    def test_practicing(self):
        print("verifying exercise--")
        startpractisingBtn = self.driver.find_element_by_id('btn_basic_example')
        startpractisingBtn.click()
        time.sleep(10)
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#basic .head')))

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
    #@pytest.mark.skip()
    #@pytest.mark.skipif(a!=b,reason="This test wants to be run on Linux machine")
    #@pytest.mark.run(order=2)
    @pytest.mark.smoke
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

    @pytest.mark.regression
    #@pytest.mark.run(order=1)
    def test_practice(self,test_setUp):
        driver.find_element_by_xpath("//*[@id='navbar']/div/div/div/ul/li[1]/a").click()
        time.sleep(10)
        title=driver.title
        print (title)
        print ("hai test_login method has been executed successfully")





