from selenium import webdriver
from selenium.webdriver.common.by import By
class HandyWrappers(object):
    def __init__(self,driver):
        self.driver=driver
        #to this constructor we passed argument in UsingWrappers() in Using_Wrappers_Demo_1(module)

#we didnt use this method also in Using_Wrappers_Demo_2
    def getBytype(self,locatertype):
        #it will convert upper case to lower case
        locatertype=locatertype.lower()
        if locatertype=="id":
            return By.ID
        elif locatertype=="xpath":
            return By.XPATH
        elif locatertype=="name":
            return By.NAME
        elif locatertype=="classname":
            return By.CLASS_NAME
        elif locatertype=="tagname":
            return By.TAG_NAME
        elif locatertype=="linktext":
            return By.LINK_TEXT
        elif locatertype=="cssselector":
            return By.CSS_SELECTOR
        else:
            print "locater type is not supported"
        return False

#we didnt use this method in Using-Wrappers_Demo_2 ,if we want we can use this method
    def getelement(self,locater,locatertype="id"):
        element=None
        try:
            locatertype=locatertype.lower()
            #this getBytype() will return the value and that value will stored in bytype variabel
            bytype=self.getBytype(locatertype)
            #here ,return value of bytype is By.Id(bytype=By.Id)
            element=self.driver.find_element(bytype,locater)
            #we passed argument to the locater in Using_Wrappers_Demo_2 module(file)
            print "element found"
        except:
            print "element not found"
        return element


#this below method will tells us whether the given web element,
#is present on the web page or not
#before doing actions on elements of a web page,
#we have to check whether the element is present on web page or no
    #if it is present ,it produces a booleen value like True
    #if is not present ,it produces a booleen value like False
    def iselementpresent(self,bytype,locater):
        #we passed arguments like (By.ID,"name") to this method in Using_Wrappers_Demo_2
        element = self.driver.find_element(bytype, locater)
        try:
           if element is not None:
              print 'element found'
              return True
           else:
              return False
        except:
            print 'element is not found'
            return False

    # before doing actions on elements of a web page,
    # we have to check whether the element is present on web page or no
    #this method also will do same as like as above method iselementpresenet()
    # this below method will tells us whether the given web element,
    # is present on the web page or not
    # if it is present ,it produces a booleen value like True
    # if is not present ,it produces a booleen value like False

    def elementpresence(self,bytype,locater):
        # we passed arguments (By.XPATH,"//input[@id='name']")to this method in Using_Wrappers_Demo_2
        elementlist = self.driver.find_elements(bytype, locater)
        try:
           length = len(elementlist)
           print ("the total no of elements are:", length)
           if len(elementlist)>0:
              print 'element found'
              return True
           else:
              return False
        except:
            print 'element is not found'
            return False


#we created obj ref var to this class in Using_Wrappers_Demo_2 (module or file)

