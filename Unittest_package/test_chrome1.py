from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options

import unittest
import time

class TestClass2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print "the setUpClass has started just now"
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    #this test will run first ..why because in the test method name we gave _01_
    def test_01_google_searchbox_python(self):
        driver=self.driver
        driver.get('http://www.google.com')
        self.assertIn("Google", driver.title)
        time.sleep(5)
        search_box = driver.find_element_by_css_selector('#tsf > div:nth-child(2) > div > div.RNNXgb > div > div.a4bIc > input')
        search_box.send_keys("python interview questions")
        search_box.submit()
        time.sleep(5)

    # this test will run first ..why because in the test method name we gave _02__
    def test_02_google_searchbox_java(self):
        driver=self.driver
        driver.get('http://www.google.com')
        self.assertIn("Google", driver.title)
        time.sleep(5)
        search_box = driver.find_element_by_css_selector('#tsf > div:nth-child(2) > div > div.RNNXgb > div > div.a4bIc > input')
        search_box.send_keys("java interview questions")
        search_box.submit()

    # this test will run first ..why because in the test method name we gave _03
    #the below method not belongs to selenium
    #we have so many assert methods are there ,plse check once
    #https://docs.python.org/3/library/unittest.html#unittest.TestCase..reffer this url

    def test_03_assert(self):
        a=10
        b=10
        #if i give a=10 , b=11 , the below assertion message will comes in the console
        self.assertEqual(a,b,"a is equal to b")
        #if a=10,b=10 , the below print msg will comes in the console
        print "assert method works properly"



    @classmethod
    def tearDownClass(cls):
        print "the tesrDownClass has ended just now"
        cls.driver.close()

if __name__=="main":
    unittest.main(verbosity=2)









