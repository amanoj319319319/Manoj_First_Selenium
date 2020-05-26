from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class DynamicXpathFormat(object):
    def test(self):
        baseurl='https://learn.letskodeit.com/p/practice'
        driver=webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(10)

        # 'Login'==How to click and type on a web element
        driver.find_element_by_xpath('//a[@href="/sign_in"]').click()
        username=driver.find_element_by_xpath("//input[@id='user_email']")
        username.send_keys('test@email.com')
        password=driver.find_element_by_id('user_password')
        password.send_keys('abcabc')
        login=driver.find_element_by_xpath("//input[@value='Log In']")
        login.click()
        #course search box
        course=driver.find_element_by_xpath('//input[@id="search-courses"]')
        course.send_keys('JavaScript')
        course.submit()

        #select course
        _course="//div[contains(@class,'course-listing-title') and contains(text(),'{}')]"
        _courselocater=_course.format('JavaScript for beginners')

        courseelement=driver.find_element_by_xpath(_courselocater)
        courseelement.click()

        time.sleep(3)
        driver.quit()

#
#course="//div[contains(@class,'course-listing-title') and contains(text(),'{0}')]",how this ,
#came means ,in the course search box first u enter JavaScript for beginners,then click enter,
#then ,inspect that 'JavaScript for beginners' title and find the path by like this ,
#course="//div[contains(@class,'course-listing-title') and contains(text(),'JavaScript for beginers')]"




dd=DynamicXpathFormat()
dd.test()