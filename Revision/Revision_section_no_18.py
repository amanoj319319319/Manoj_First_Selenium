'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Browser_interactions():
    def Interaction(self):
        driver=webdriver.Firefox()
        baseurl='https://learn.letskodeit.com/p/practice'

        driver.maximize_window()
        print "window has been maximized"
        driver.get(baseurl)
        title1=driver.title
        print ("The title name is :",title1)
        currenturl=driver.current_url
        print ("The current url is :",currenturl)

        driver.refresh()
        print ("The current page has been refreshed for the first time")
        driver.get(driver.current_url)
        print ("The current page has been refreshed again second time")

        driver.get('https://sso.teachable.com/secure/42299/users/sign_in?clean_login=true&reset_purchase_session=1')
        print ("now we are in another url")

        driver.back()
        print ("we came back to the first url")

        driver.forward()
        print ("we move another url again")

        pagesource=driver.page_source
        print pagesource

        driver.close()
        driver.quit()

ee=Browser_interactions()
ee.Interaction()
'''

#How to click and Find an elements on the webpage
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Elements_Perfom():
    def Interaction(self):
        driver=webdriver.Firefox()
        baseurl='https://learn.letskodeit.com/p/practice'
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(10)

        Login_Link=driver.find_element(By.XPATH, '//*[@id="navbar"]/div/div/div/ul/li[2]/a')
        Login_Link.click()

        Username=driver.find_element(By.XPATH, '//input[@id="user_email"]')
        Username.send_keys("manoj")

        Password=driver.find_element(By.XPATH, '//input[@id="user_password"]')
        Password.send_keys("123456")

        time.sleep(3)

        Username.clear()

        Username.send_keys("selenium")




ee=Elements_Perfom()
ee.Interaction()

'''

#how to find out state of the elements(enabled/disabled)
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Enabled_or_Disable():
    def Interaction(self):
        driver=webdriver.Firefox()
        baseurl='https://www.google.com/'
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(10)

        Search_box=driver.find_element(By.XPATH, '//*[@id="tsf"]/div[2]/div/div[1]/div/div[1]/input')
        isenabel=Search_box.is_enabled()
        print ("is this element enabled?:",isenabel)
        Search_box.send_keys("python interview questions")
        Search_box.submit()

ee=Enabled_or_Disable()
ee.Interaction()

#If any element has disabled , we can perform any actions on that element.
#how can we find the element is disable means , when you inspect that element , you can see ,
#one attribute like disabled=""...with we can conform like this element is disabled .

'''

#working on Radio buttons and Check boxes
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Radiobuttons_Checkboxes():
    def Interaction(self):
        driver=webdriver.Firefox()
        baseurl='https://learn.letskodeit.com/p/practice'
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(10)

        BMWradio_button=driver.find_element(By.ID, "bmwradio")
        BMWradio_button.click()
        time.sleep(3)
        BENZradio_button=driver.find_element(By.ID, "benzradio")
        BENZradio_button.click()
        time.sleep(3)

        BMWcheck_box=driver.find_element(By.ID, "bmwcheck")
        BMWcheck_box.click()
        time.sleep(3)
        BENZcheck_box=driver.find_element(By.ID, "benzcheck")
        BENZcheck_box.click()

        #we have one method like is_selected()..it helps for both radio buttons and check boxes
        print ("is BMW radio button is selected?",BMWradio_button.is_selected())
        print ("is BENZ radio button is selected?", BENZradio_button.is_selected())
        print ("is BMW check box is selected?", BMWradio_button.is_selected())
        print ("is BENZ check box is selected?", BMWradio_button.is_selected())


rr=Radiobuttons_Checkboxes()
rr.Interaction()

'''

#working with Radio buttons elements list
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class WorkingWithElementsList():

    def testListOfElements(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        radioButtonsList = driver.find_elements(
            By.XPATH, "//input[contains(@type,'radio') and contains(@name,'cars')]")
        size = len(radioButtonsList)
        print("Size of the list: " + str(size))

        for radioButton in radioButtonsList:
            isSelected = radioButton.is_selected()

            if not isSelected:
                radioButton.click()
                time.sleep(2)

ff = WorkingWithElementsList()
ff.testListOfElements()

'''

#how to work with dropdown elements
#this select class works only for the elements who has select tag
'''
from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

class DropdownSelect():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        element = driver.find_element_by_id("carselect")
        sel = Select(element)

        sel.select_by_value("benz")
        print("Select Benz by value")
        time.sleep(2)

        sel.select_by_index("2")
        print("Select Honda by index")
        time.sleep(2)

        sel.select_by_visible_text("BMW")
        print("Select BMW by visible text")
        time.sleep(2)

        sel.select_by_index(2)
        print("Select Honda by index")


ff = DropdownSelect()
ff.test()

'''

#working with HIDDEN elements
'''
from selenium import webdriver
import time

class HiddenElements():

    def testLetsKodeIt(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(2)


        # Find the state of the text box
        textBoxElement = driver.find_element_by_id("displayed-text")
        textBoxState = textBoxElement.is_displayed() # True if visible, False if hidden
        # Exception if not present in the DOM
        print("Text is visible? " + str(textBoxState))
        time.sleep(2)

        # Click the Hide button
        driver.find_element_by_id("hide-textbox").click()
        # Find the state of the text box
        textBoxState = textBoxElement.is_displayed()
        print("Text is visible? " + str(textBoxState))
        time.sleep(2)

        # Added code to scroll up because the element was hiding behind the top navigation menu
	# You will learn about scrolling in future lecture
        driver.execute_script("window.scrollBy(0, -150);")
        # Click the Show button
        driver.find_element_by_id("show-textbox").click()
        # Find the state of the text box
        textBoxState = textBoxElement.is_displayed()
        print("Text is visible? " + str(textBoxState))
        time.sleep(2)
        # Browser Close
        driver.quit()

    def testExpedia(self):
        baseUrl = "http://www.expedia.com"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        driver.find_element_by_id("tab-flight-tab").click()

        drpdwnElement = driver.find_element_by_id("flight-age-select-1")
        print("Element visible? " + str(drpdwnElement.is_displayed()))


ff = HiddenElements()
ff.testLetsKodeIt()
ff.testExpedia()
'''

'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

class dropdown():
    def drop(self):
        driver=webdriver.Firefox()
        baseurl='https://learn.letskodeit.com/p/practice'
        driver.get(baseurl)
        driver.maximize_window()
        driver.implicitly_wait(10)

        show=driver.find_element(By.ID, "show-textbox")
        show.click()
        display_text=driver.find_element(By.ID, "displayed-text")
        print ("is show button is displayed:",display_text.is_displayed())
        time.sleep(3)

        hide=driver.find_element(By.ID, 'hide-textbox')
        hide.click()
        display_text = driver.find_element(By.ID, "displayed-text")
        print ("is hide button is displayed:",display_text.is_displayed())
        time.sleep(3)

        show = driver.find_element(By.ID, "show-textbox")
        show.click()
        display_text = driver.find_element(By.ID, "displayed-text")
        print ("is show button is displayed:", display_text.is_displayed())

d=dropdown()
d.drop()
'''