"""
http://pytest-ordering.readthedocs.io/en/develop/
"""

import pytest
import sys
from conftest1 import setUp
from conftest1 import oneTimeSetUp

#how to run our test cases in order wise
#i want to run my test cases in the below order wise
# B, A, C, E, D
@pytest.mark.run(order=2)
def test_run_order_methodA(oneTimeSetUp, setUp):
    print("Running method A")

@pytest.mark.run(order=1)
def test_run_order_methodB(oneTimeSetUp, setUp):
    print("Running method B")

@pytest.mark.run(order=3)
def test_run_order_methodC(oneTimeSetUp, setUp):
    print("Running method C")

@pytest.mark.run(order=5)
def test_run_order_methodD(oneTimeSetUp, setUp):
    print("Running method D")

@pytest.mark.run(order=4)
def test_run_order_methodE(oneTimeSetUp, setUp):
    print("Running method E")

#how to skip the particular method
@pytest.mark.skip(reason="no need to run this method right now")
def test_run_order_methodF(oneTimeSetUp, setUp):
    print("Running method F")


@pytest.mark.skipif(sys.version>3.5, reason="no need to run this method right now")
def test_run_order_methodG(oneTimeSetUp, setUp):
    print("Running method G")

@pytest.mark.run(order=6)
def test_RUN_order_methodH(oneTimeSetUp, setUp):
    print("Running method H")


#how to run the particular method , .. pytest -k method name -v
#if we execute like this , it will run only one method which we written in the syntax

#if i want to learn the test methids who has (_RUN_)in between the methods ,we should run ,
#like this .. pytest -k _RUN -v ...in the above code _RUN is in only test_RUN_order_methodH

