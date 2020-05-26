'''
import pytest
#If we want to write any fixcture , first we need to write one method ,after that with ,
#the help of the decorater we can write the fixture.
#If you want to aplly the fixture to any method , you need to pass the fixture name as a parameter,
#to the method

@pytest.fixture()
def setUp():
    print ("setUp fixture will run before every methoddddddddddddd")

def test_methodA(setUp):
    print "this is method AAAAAAAA"

def test_methodB(setUp):
    print "this is method BBBBBBBB"

'''

'''
def test_methodAA(onetimesetUp,setUp):
    print "this is method AAAAAAAA"

def test_methodBB(onetimesetUp,setUp):
    print "this is method BBBBBBBB"

def test_hi_statement():
    print "hi to all"
'''

#structire tests in a class
'''
How to use test class to wrap methods under one class
Learn about autouse keywords in fixtures
Assert the result to create a real test scenario
'''

class SomeClassToTest():

    def __init__(self, value):
        self.value = value


    def sumNumbers(self, a, b):
        return a + b + self.value