#Data Driven Testing using Unit Test ... its really simply superb
'''
import unittest
from ddt import ddt, data, unpack
from selenium import webdriver
import time
@ddt
class letskode(unittest.TestCase):
    @data(("manoj",),("jyothi",))#it is a tuple , we can provide values to the webelements using tuple.
    def test_code(self,a):
        driver=webdriver.Chrome()
        driver.maximize_window()
        url="https://learn.letskodeit.com/p/practice"
        driver.get(url)
        ab=driver.find_element_by_id("name")
        ab.click()
        ab.send_keys(a)
        time.sleep(4)
unittest.main()
'''
