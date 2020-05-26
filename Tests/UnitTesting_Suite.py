#First way without generating HTML Reports for the modules whichever we have imported

from selenium import webdriver
import unittest
import HtmlTestRunner
#Importing modules into this file

from UnitTesting_1 import Login_Test
from UnitTesting_2 import Switch_Test

#Loading Test methods of the Test cases which were imported by this file
tc1=unittest.TestLoader().loadTestsFromTestCase(Login_Test)
tc2=unittest.TestLoader().loadTestsFromTestCase(Switch_Test)

#Creating test suite for combining both Login_Test and Switch_test
ts=unittest.TestSuite([tc1,tc2])
unittest.TextTestRunner().run(ts)


#Second way is that generating HTML Reports for the modules whichever we have imported
'''
from selenium import webdriver
import unittest
import HtmlTestRunner

from UnitTesting_1 import Login_Test
from UnitTesting_2 import Switch_Test
import os

#Creating test suite for the test classes whichever we have imported by us in this module 
consolidated_list=unittest.TestSuite()

#Adding tests or loading tests 
consolidated_list.addTests([unittest.defaultTestLoader.loadTestsFromTestCase(Login_Test),
                            unittest.defaultTestLoader.loadTestsFromTestCase(Switch_Test)])
                            
#destination of the html file 
output_file = open("C:\Users\Manoj\PycharmProjects\FirstSeleniumTest\REPORTS_UNITTESTING" + "\HTML_Test_2.html", "w")

html_runner = HtmlTestRunner.HTMLTestRunner(
    stream=output_file)

html_runner.run(consolidated_list)
'''




