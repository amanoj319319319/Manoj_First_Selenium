from selenium import webdriver
from selenium.webdriver.common.by import By
from A_Pages.test_facebook_loginpage import LoginPage
import unittest

class LoginTests(unittest.TestCase):

    def test_validLogin(self):
        baseURL = "https://www.facebook.com/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)

        lp = LoginPage(driver)
        lp.login("a.manoj16@gmail.com", "santhuji")


