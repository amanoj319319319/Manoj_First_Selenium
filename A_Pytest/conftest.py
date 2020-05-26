'''
import pytest
from selenium import webdriver

@pytest.yield_fixture(scope="class")
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

'''
import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    print("initiating chrome driver")
    global driver
    driver = webdriver.Chrome("chrome driver path") #if not added in PATH
    driver.get("http://seleniumeasy.com/test")
    driver.maximize_window()
    request.cls.driver = driver

    yield driver
    driver.close()

'''

'''
import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def setup(request):
    print("initiating chrome driver")
    global driver
    driver = webdriver.Chrome()
    session = request.node
    for item in session.items:
        cls = item.getparent(pytest.Class)
        setattr(cls.obj, "driver", driver)
    driver.get("https://learn.letskodeit.com/")
    driver.maximize_window()

    yield driver
    driver.close()

'''


import pytest
from selenium import webdriver
from webdriverfactory import WebDriverFactory

@pytest.yield_fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")


@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, browser):
    print("Running one time setUp")
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
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