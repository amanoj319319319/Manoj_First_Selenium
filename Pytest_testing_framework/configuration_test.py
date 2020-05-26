'''
import pytest

@pytest.yield_fixture()
def setUp():
    print ("setUp yield_fixture will run before every method")
    yield
    print ("setUp yield_fixture will run after every method")

#observe the diff between two fixtures above one and below one
#the below fixture method will run only one time before module of a method and one time after,
#a module of a method

@pytest.yield_fixture()
def onetimesetUp(scope="module"):
    print ("onetimesetUp will run only one time for a module before the first test method")
    yield
    print ("onetimesetUp will run only one time for a module after the last test method")
'''

#how do we run the tests based on commond line argumentss
"""
import pytest

@pytest.yield_fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")


@pytest.yield_fixture(scope="module")
def oneTimeSetUp(browser):
    print("Running one time setUp")
    if browser == 'firefox':
        print("Running tests on FF")
    else:
        print("Running tests on chrome")
    yield
    print("Running one time tearDown")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="module")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="module")
def osType(request):
    return request.config.getoption("--osType")
"""

#structire tests in a class

import pytest

@pytest.yield_fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")


@pytest.yield_fixture(scope="class")
def oneTimeSetUp(browser):
    print("Running one time setUp")
    if browser == 'firefox':
        print("Running tests on FF")
    else:
        print("Running tests on chrome")
    yield
    print("Running one time tearDown")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")

