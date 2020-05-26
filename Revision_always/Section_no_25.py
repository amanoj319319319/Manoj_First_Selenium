##how to run the unittest code in the terminal...below is the syntax
#py.test -s -v packagename/filename.py
#you have run this unit test code only in terminal , then only u can able to see all the methods,'
#print statements
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
class TestClass1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print "class level group1"
        print "i run onlyy once before executing all the methods"
    def setUp(self):
        print "i am with out classmethod"
        print "i run evrey time before the method"
    def test_method_a(self):
        print "i am method A"
    def test_method_b(self):
        print "i am method B"
    def tearDown(self):
        print "i am with out class method"
        print "i run every time before each method"
    @classmethod
    def tearDownClass(cls):
        print "class level group2"
        print "i run only once after all the methods got executed"

if __name__ == "main":
    unittest.main(verbosity=2)

'''