import pytest
#If we want to write any fixcture , first we need to write one method ,after that with ,
#the help of the decorater we can write the fixture.
#If you want to aplly the fixture to any method , you need to pass the fixture name as a parameter,
#to the method

'''
@pytest.fixture()
def setUp():
    print ("setUp fixture will run before every method")

def test_methodA(setUp):
    print "this is method A"

def test_methodB(setUp):
    print "this is method A"
'''

#pytest conventions are ..
#filename should starts with test_ and class name starts with Test and method name starts with test_

#If i run like this .. pytest -s -v (it will run all the pytest moules which are associated with ,
#the pytest



#This yield_fixture() is also one kind of pytest fixcture
#before the yield whatever the code is there ,it works after the method only
#after the yield whatever the code is there ,it works after the method only
#you can the pytest code like this also ,
#1st way ...pytest -s -v packagename/filename.py
#2nd way ...py.test -s -v packagename/filename.py
#we cant run the pytest code modules in the console by right clicking
#we should run compulsarily in Terminal
'''
@pytest.yield_fixture()
def setUp():
    print ("setUp yield_fixture will run before every method")
    yield
    print ("setUp yield_fixture will run after every method")

def test_methodA(setUp):
    print "this is method A"

def test_methodB(setUp):
    print "this is method A"

#OR
#instead of @pytest.yield_fixcture() , if we use @pytest.fixcture() also the below code will works.
@pytest.fixture()
def setUp():
    print ("setUp yield_fixture will run before every method")
    yield
    print ("setUp yield_fixture will run after every method")

def test_methodA(setUp):
    print "this is method A"

def test_methodB(setUp):
    print "this is method A"

'''



#How do we run the pytest modules in diff ways
#the below three ways highly used
#1st way is .. py.test -s -v packagename/filename.py
#2nd way is .. py.test -s -v somepath
#3rd way is .. py.test -s -v packagename/filename.py/methodname
'''
@pytest.fixture()
def setUp():
    print ("setUp yield_fixture will run before every method")
    yield
    print ("setUp yield_fixture will run after every method")

def test_methodA(setUp):
    print "this is method A"
def test_methodB(setUp):
    print "this is method B"

'''


'''
from Pytest_testing_framework.configuration_test import setUp
from Pytest_testing_framework.configuration_test import onetimesetUp
#below three are importing methods of test_class2.py
from Pytest_testing_framework.test_case2 import test_methodAA
from Pytest_testing_framework.test_case2 import test_methodBB
from Pytest_testing_framework.test_case2 import *
#that setUp and onetimesetUp fixture methods will works on the methods of test_class2.py,why because ,
#we imported them in this moudle and also we passed fixture methods in test_class2.py methods
#plse reffer configuration_test.py

def test_methodA(onetimesetUp,setUp):
    print "this is method A"
def test_methodB(onetimesetUp,setUp):
    print "this is method B"

if __name__=="main":
    pytest.main()

'''


#How do we run the test cases in an order wise.
'''
from Pytest_testing_framework.configuration_test import setUp
from Pytest_testing_framework.configuration_test import onetimesetUp


@pytest.mark.run(order=2)
def test_methodA(onetimesetUp,setUp):
    print "this is method A"
    print "according to the order , it will execute after the execution of test_methodB"
@pytest.mark.run(order=1)
def test_methodB(onetimesetUp,setUp):
    print "this is method B"
    print "according to the order , it will execute before the execution of test_methodA"

if __name__=="main":
    pytest.main()

'''
#how do we run the tests based on commond line argumentss
'''
from Pytest_testing_framework.configuration_test import setUp
from Pytest_testing_framework.configuration_test import oneTimeSetUp

def test_command_line_methodA(oneTimeSetUp, setUp):
    print("Running method A")

def test_command_line_methodB(oneTimeSetUp, setUp):
    print("Running method B")

if __name__=="main":
    pytest.main()


'''


#structire tests in a class
'''
import pytest
from Pytest_testing_framework.test_case2 import  SomeClassToTest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestClassDemo():

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.abc = SomeClassToTest(10)

    def test_methodA(self):
        result = self.abc.sumNumbers(2, 8)
        assert result == 20
        print("Running method A")

    def test_methodB(self):
        print("Running method B")

'''

@pytest.fixture()
def setUp():
    print ("setUp fixture will run before every method")

def test_methodA(setUp):
    print "this is method A"

def test_methodB(setUp):
    print "this is method A"







