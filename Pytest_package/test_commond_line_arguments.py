import pytest
#reffer conftest.py file in Pytest_package

def test_command_line_methodA(oneTimeSetUp, setUp):
    print("Running method A")

def test_command_line_methodB(oneTimeSetUp, setUp):
    print("Running method B")