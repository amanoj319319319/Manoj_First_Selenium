#in the below code , we combined the two files to gether and we ran them in single action
'''
import unittest
from Revision.Unittest_Testsuite_1 import TestClass1
from Revision.Unittest_Testsuite_2 import TestClass2

import unittest
from Revision.Unittest_Testsuite_1 import TestClass1
from Revision.Unittest_Testsuite_2 import TestClass2

# Get all tests from TestClass1 and TestClass2
tc1 = unittest.TestLoader().loadTestsFromTestCase(TestClass1)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestClass2)

# Create a test suite combining TestClass1 and TestClass2
smokeTest = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner(verbosity=2).run(smokeTest)

'''