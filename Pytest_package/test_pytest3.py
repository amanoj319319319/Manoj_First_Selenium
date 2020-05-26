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

import pytest
from conftest1 import setUp
from conftest1 import oneTimeSetUp

def test_demo2_methodA(oneTimeSetUp,setUp):
    print("Running demo2 method A")

def test_demo2_methodB(oneTimeSetUp,setUp):
    print("Running demo2 method B")
