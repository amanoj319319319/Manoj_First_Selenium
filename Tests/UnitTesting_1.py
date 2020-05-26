from selenium import webdriver
import unittest
import time
import HtmlTestRunner

class Login_Test(unittest.TestCase):
    #Implementing unittest setUp method mechanism
    def setUp(self):
        print ("i will print only once before executing each test case of a Login_Test class")
        self.driver=webdriver.Chrome()
        url="https://letskodeit.teachable.com/"
        self.driver.get(url)
        time.sleep(3)

    #@unittest.SkipTest
    def test_Login(self):
        self.driver.find_element_by_xpath("//*[@id='navbar']/div/div/div/ul/li[2]/a").click()
        time.sleep(3)
        title_of_webpage=self.driver.title
        self.assertEqual(title_of_webpage,self.driver.title,"web page title is not matched")

    a=10
    b=20

    #@unittest.skip("This method still has to be implemented more...")
    #@unittest.skipIf(a != b,"Letters are not equal") ,when given condition becomes True then only the test case will be skipped
    def test_Practice(self):
        self.driver.find_element_by_xpath("//*[@id='navbar']/div/div/div/ul/li[1]/a").click()
        time.sleep(3)
        title_of_webpage=self.driver.title
        print (title_of_webpage)
        self.assertEqual(title_of_webpage,self.driver.title,"web page title is not matched")

    # Implementing unittest tearDown method mechanism
    def tearDown(self):
        print ("i will print only once before executing each test case of a Login_Test class")
        self.driver.quit()

#if __name__ == "__main__":
#    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:\\Users\\Manoj\\PycharmProjects\\FirstSeleniumTest\\REPORTS_UNITTESTING"))




