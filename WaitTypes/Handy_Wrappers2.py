from selenium.webdriver.common.by import By
class HandyWrappers():
    def __init__(self,driver):
        self.driver=driver
        #to this constructor we passed argument in UsingWrappers() in Using_Wrappers_Demo_1(module)

#we didnt use this method also in Using_Wrappers_Demo_2
    def getBytype(self,locatertype='id'):
        #it will convert upper case to lower case
        locatertype=locatertype.lower()
        if locatertype=="id":
            return 'By.ID'
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

    def getelement(self,locater,locatertype="id"):
        element=None
        try:
            locatertype=locatertype.lower()
            #this getBytype() will return the value and that value will stored in bytype variabel
            bytype=self.getBytype(locatertype)
            #here ,return value of bytype is By.Id(bytype=By.Id)
            element=self.driver.find_element(bytype, locater)
            #we passed argument to the locater in Using_Wrappers_Demo_2 module(file)
            print "element found"
        except:
            print "element not found"
        return element

