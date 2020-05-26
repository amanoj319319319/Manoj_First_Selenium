#Finding an effective xpaths
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class EffectiveXpath():
    def path(self):
        driver=webdriver.Firefox()
        baseurl='https://learn.letskodeit.com/p/practice'
        driver.get(baseurl)
        #baseurl1 = 'https://learn.letskodeit.com/'
        #driver.get(baseurl1)
        driver.maximize_window()
        driver.implicitly_wait(10)

        #Syntax of finding Xpath
        # //Tag[@attribute="value"] .. with this syntax ,we can able to find aany locater on page
        #Finding an Xpath for webelement like switch to alert example on our practice page

        #Element1=driver.find_element_by_xpath('//input[@id="name"]')
        #Element1.send_keys("hi")

        # Finding an Xpath for webelement like switch to alert example on our practice page
        #Element2=driver.find_element_by_xpath('//input[@name="enter-name"]')
        #Element2.send_keys("hi")


        #building Relative Xpath by using double slash( // ) for element
        # Finding an Xpath for webelement like switch to alert example on our practice page
        #Element3=driver.find_element_by_xpath('//div//fieldset//input[@id="name"]')
        #Element3.send_keys("hi")

        #building Relative Xpath by using double slash( / ) for element
        #Finding an Xpath for webelement like switch to alert example on our practice page
        #Element4=driver.find_element_by_xpath('//div[@id="navbar"]/div/div/div/ul/li[2]//a')
        #Element4.click()

        #building Relative Xpath by using double slash( / ) for element
        #Finding an Xpath for webelement like switch to Enroll now on our below link
        #'https://learn.letskodeit.com/'
        #Element5=driver.find_element_by_xpath('//div[@id="block-1754138"]/div/div/div/a')
        #Element5.click()

        #using Text() of the element to build Xpath
        #the text should be in between tags like (ex:- >Enroll now<
        # Finding an Xpath for webelement like Enroll now on our below link
        # 'https://learn.letskodeit.com/'
        #Element6=driver.find_element_by_xpath('//div[@id="block-1754138"]//a[text()="Enroll now"]')
        #Element6.click()

        #using contains method to find elements on the web page
        #Syntax is :- //Tag[contains(@attribute, value)]
        #we performed action on switch to alert example
        #Element7=driver.find_element_by_xpath('//input[contains(@id,"name")]')
        #Element7.send_keys("hi")

        # using contains method to find elements on the web page
        #we performed an action on Login link on our practice page
        #Element8=driver.find_element_by_xpath('//div[@id="navbar"]//a[contains(text(), "Login")]')
        #Element8.click()

        #using double times contains method to find an element
        #we performed action on swtch to alert element on webpage
        #Element8=driver.find_element_by_xpath('//input[contains(@id, "name") and contains(@name, "enter-name")]')
        #Element8.send_keys("hi")

        #finding an element using starts_with on webpage
        # we performed action on swtch to alert element on webpage
        #Syntax is : //Tag[starts-with(@attribute, value)]
        #Element9=driver.find_element_by_xpath('//input[starts-with(@id, "name")]')
        #Element9.send_keys("hi")

        #we performed an action on Login link with id as well as with starts-with on our practice page
        #Element10=driver.find_element_by_xpath('//div[@id="navbar"]//a[starts-with(@class, "navbar-link fedora-navbar-link")]')
        #Element10.click()


        #we found an Xpath for the table elemenet of python programming language price 30
        #Element11=driver.find_element_by_xpath('//table[@id="product"]/tbody/tr[3]/td[2]//following-sibling::td')



ee=EffectiveXpath()
ee.path()

# we can able to get the Absolute Xpth from the Firefox browser. just inspect an element ,
#do right click ,copy ,xpath.....Thats it .you can use this Absolute xpath in Chrome also .

'''

'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class EffectiveXpath():
    def path(self):
        driver=webdriver.Firefox()
        baseurl='https://learn.letskodeit.com'
        driver.get(baseurl)
        driver.maximize_window()
        driver.implicitly_wait(10)

        Element=driver.find_element(By.XPATH, '//*[@id="block-1754138"]/div/div/div/a')
        Element.click()

        text_get=Element.text
        print text_get

ee=EffectiveXpath()
ee.path()

'''