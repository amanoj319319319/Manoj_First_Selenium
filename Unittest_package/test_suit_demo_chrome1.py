#it works very fine
#This is Test suit...very very imp

import unittest
from Unittest_package.test_case_demo1 import TestClass1
from Unittest_package.test_chrome1 import TestClass2

# Get all tests from TestClass1 and TestClass2
tc1 = unittest.TestLoader().loadTestsFromTestCase(TestClass1)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestClass2)

# Create a test suite combining TestClass1 and TestClass2
smokeTest = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner(verbosity=2).run(smokeTest)

if __name__=="main":
    unittest.main()

#In real time scenario , we dont run each test module seperately ,
#we grouped all the test modules in to one module ie nothing but Test Suit,
#we should create a test suite to run all the test modules at a time in one place