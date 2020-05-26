#how to run the pytest code in the terminal...below has the syntax
#py.test -s -v packagename/filename.py
'''
import pytest
@pytest.yield_fixture()
def setUp():
    print("Running demo2 setUp")
    yield
    print("Running demo2 tearDown")

def test_demo2_methodA(setUp):
    print("Running demo2 method A")

def test_demo2_methodB(setUp):
    print("Running demo2 method B")

'''
#how to run the pytest code in the terminal...below has the syntax
#py.test -s -v packagename/filename.py
'''
import pytest

@pytest.fixture()
def setUp():
    print("Running demo1 setUp")

def test_demo1_methodA(setUp):
    print("Running demo1 method A")

def test_demo1_methodB(setUp):
    print("Running demo1 method B")

'''
#how to run the pytest test cases
#1st way .. py.test -s -v packagename/filename.py
#2nd way .. py.test -s -v (if we run like this , all the pytest files which are under the pytest,
#package will run
#3rd way .. py.test -s -v packagename/filename.py::methodname
#the above all the three ways will works only in terminal
