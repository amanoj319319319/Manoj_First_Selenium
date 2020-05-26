'''
import unittest

class TestCaseDemo1(unittest.TestCase):

    def setUp(self):
        print("I will run once before every testdemo")

    def test_methodA(self):
        print("Running method A")

    def test_methodB(self):
        print("Running method B")

    def tearDown(self):
        print("I will run after every testdemo")

if __name__ == '__main__':
    unittest.main(verbosity=2)

'''

#class level setUp and tearDown methods
#if we use class level setUp and tearDown methods ,these two will run only once,
#that is before method execution setUp class level method will execute ,and,
#after executing the all the methods which are defined under this setUp class level method ,
#the tearDown class level method will execute only once
'''
import unittest

class TestCaseDemo2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("*#" * 30)
        print("I will run only once before all tests")
        print("*#" * 30)

    def setUp(self):
        print("I will run once before every testdemo")

    def test_methodA(self):
        print("Running method A")

    def test_methodB(self):
        print("Running method B")

    def tearDown(self):
        print("I will run after every testdemo")

    @classmethod
    def tearDownClass(cls):
        print("*#" * 30)
        print("I will run only once after all tests")
        print("*#" * 30)


if __name__ == '__main__':
    unittest.main(verbosity=2)

'''
#How to Assert a Test method
"""
https://docs.python.org/3/library/unittest.html#unittest.TestCase
"""

'''
import unittest

class AssertDemo(unittest.TestCase):

    def test_assertTrueFalse(self):
        a = True
        self.assertTrue(a, "a is not false")
        #("a is not false" is msg parameter)
        #why will we write msgs means , if anything wrong , we should tell the user right one,
        #nothing but we are showing a way to user where he did the mistake
        b = False
        self.assertFalse(b, "b is not true")

    def test_assertEqual(self):
        a = "Test"
        b = "test"
        self.assertEqual(a, b, msg="'a' is not equal to 'b'")


if __name__ == '__main__':
    unittest.main(verbosity=2)

'''

#How to run code from terminal
#Go to Terminal which is available in the bottom side of the PyCharm IDE
#once it has opened , you can run python file as like as same in our original commond prompt like,
#python packagename/filename