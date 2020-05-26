from selenium import webdriver
import unittest
import time
import HtmlTestRunner

class Switch_Test(unittest.TestCase):
    @classmethod
    #implementing unittest setUpClass mechanism
    def setUpClass(cls):
        print ("i will run only once befoe execting all the test cases of a Switch_Test class")
        cls.driver=webdriver.Chrome()
        url="https://learn.letskodeit.com/p/practice"
        cls.driver.get(url)
        time.sleep(3)
    '''
    def setUp(self):
        self.driver=webdriver.Chrome()
        url="https://learn.letskodeit.com/p/practice"
        self.driver.get(url)
        time.sleep(3)
    '''

    def test_Switch_to_alert_example(self):
        self.driver.find_element_by_id("name").send_keys("manoj")
        time.sleep(3)
        title_of_webpage=self.driver.title
        self.assertEqual("practice ",self.driver.title,"web page title is not matched")

    @classmethod
    # implementing unittest tearDownClass mechanism
    def tearDownClass(cls):
        print ("i will run only once after execting all the test cases of a Switch_Test class")
        cls.driver.quit()

    '''   
    def tearDown(self):
        self.driver.quit()
    '''

#if __name__ == "__main__":
#    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:\\Users\\Manoj\\PycharmProjects\\FirstSeleniumTest\\REPORTS_UNITTESTING"))



