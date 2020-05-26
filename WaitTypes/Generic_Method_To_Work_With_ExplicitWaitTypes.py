'''
from traceback import print_stack
from Handy_Wrappers2 import HandyWrappers
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

class Explicitwaittype():
    def __init__(self,driver):
        self.driver=driver
        self.hw=HandyWrappers(driver)

    def waitForElement(self,locater,locatertype='id',
                           timeout=10, pollFrequency=0.5):

        element=None
        try:
            bytype=self.hw.getBytype(locatertype)
            print ("waiting for max :",str(timeout),+"for element to be clickable")
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=pollFrequency, ignored_exceptions=[NoSuchElementException,
                                                                                    ElementNotVisibleException,
                                                                                    ElementNotSelectableException])

            element = wait.until(EC.element_to_be_clickable((bytype, locater)))
            print 'element appeared on the webpage'
        except:
            print 'element not appeared on the web page'
            print_stack()
        return element
'''

from traceback import print_stack
from Handy_Wrappers2 import HandyWrappers
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

class Explicitwaittype():
    def __init__(self,driver):
        self.driver=driver
        self.hw=HandyWrappers(driver)

    def waitForElement(self,locater,locatertype='id',
                           timeout=10, pollFrequency=2):

        element=None
        try:
            bytype=self.hw.getBytype(locatertype='id')
            print ("waiting for max :",str(timeout),+"for element to be clickable")
            wait = WebDriverWait(self.driver, 10, poll_frequency=2, ignored_exceptions=[ElementNotSelectableException,
                                                                                        ElementNotInteractableException,
                                                                                        ElementNotVisibleException])
            element1=wait.until(EC.element_to_be_clickable((bytype, "stopFilter_stops-0")))

            print 'element appeared on the webpage'
        except:
            print 'element not appeared on the web page'
            print_stack()
        return element


