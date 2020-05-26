#import pytest
'''
@pytest.yield_fixture()
def setUp():
    print ("i will be printed before each test method of a test module")
    yield
    print ("i will be printed after each test method of a test module")


@pytest.yield_fixture(scope="module")
def OneTimesetUp():
    print ("OneTimesetUp will be printed starting test method of a test module")
    yield
    print ("OneTimesetUp will be printed ending test method of a test module")
'''

'''
from selenium import webdriver
import time
@pytest.yield_fixture(scope="class")
def OneTimesetUp(request,browser,OsType):
    print ("Running one time setUp")
    global driver
    if browser=="firefox":
        print ("Running tests on firefox")
        driver=webdriver.Firefox()
        driver.get("https://learn.letskodeit.com/")
    else:
        print ("Running tests on Chrome")
        driver=webdriver.Chrome()
        driver.get("https://learn.letskodeit.com/")
    yield
    print ("Running one time tear Down")
    time.sleep(2)
    driver.close()


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--ostype")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def OsType(request):
    return request.config.getoption("--ostype")

'''

'''
import pytest
from selenium import webdriver

@pytest.yield_fixture(scope="session")


def oneTimeSetUp(request):
    print("Running one time setUp")
    #if browser == 'firefox':
    baseURL = "https://letskodeit.teachable.com/"
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.get(baseURL)
    print("Running tests on FF")

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("Runni2ng one time tearDown")
'''
