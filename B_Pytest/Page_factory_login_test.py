#Writing Login page with page factory methods ........
#Refer this url .. https://pypi.org/project/selenium-page-factory/
from seleniumpagefactory.Pagefactory import PageFactory
import unittest
from selenium import webdriver
import time

class LoginPage(PageFactory):
    def __init__(self,driver):
        # It is necessary to to initialise driver as page class member to implement Page Factory
        self.driver = driver

    # define locators dictionary where key name will became WebElement using PageFactory
    locators = {
        "Text_UserName": ('ID', 'email'),
        "Text_Password": ('ID', 'pass'),
        "Button_Login": ('XPATH', '//*[@id="u_0_b"]')}

    def Login(self):
        self.Text_UserName.set_text("a.manoj16@gmail.com")
        self.Text_Password.set_text("xyzxyzxyz")
        self.Button_Login.click_button()

class LoginTest(unittest.TestCase):
    #This test will going to be executed on chrome browser
    def test_Login(self):
        driver = webdriver.Chrome()
        driver.get("https://www.facebook.com/")
        driver.maximize_window()
        time.sleep(4)
        pglogin = LoginPage(driver)
        pglogin.Login()

if __name__ == "__main__":
     unittest.main()


#WebElements Methods in page factory
'''
set_text
get_text
clear_text
click_button
get_list_item_count
select_element_by_text
select_element_by_index
select_element_by_value
get_all_list_item
get_list_selected_item
hover
is_Checked
getAttribute
element_to_be_clickable
invisibility_of_element_located
visibility_of_element_located
Note: Every WebElement will be created after verifying it's Presence and visibility on Page at Run-Time.
'''