
'''
import pytest
import sys

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

'''


import pytest

@pytest.mark.windows
def test_method_windows_A():
    print "this is method A which runs on windows"

@pytest.mark.windows
def test_method_windows_B():
    print "this is method B which runs on windows"

@pytest.mark.mac
def test_method_mac_C():
    print "this is method C which runs on windows"

@pytest.mark.mac
def test_method_mac_D():
    print "this is method D which runs on windows"

#if you want to run the tests accordings tag wise(@pytest.mark.windows) ,we can do like this,
#syntax is.. pytest -m windows -v