#working with handles,nothing but switching to the another window
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Handle():
    def window(self):
        driver = webdriver.Firefox()
        baseurl = 'https://learn.letskodeit.com/p/practice'
        driver.execute_script("window.location='https://learn.letskodeit.com/p/practice';")
        driver.maximize_window()
        driver.implicitly_wait(10)

        #finding the current window hadle name
        parent_handle=driver.current_window_handle
        print parent_handle

        #finding the element on the curent window page
        #to find open window handle we need to find out the open window element
        driver.find_element(By.ID, "openwindow").click()
        time.sleep(6)

        #finding the multiple handles
        multiple_handles=driver.window_handles
        print multiple_handles

        #how to work with the open window handle page
        for handle in multiple_handles:
            print handle
            if handle not in parent_handle:
                driver.switch_to.window(handle)
                #now we are on the open window page
                #now i am going to work with open window page web elements
                time.sleep(10)
                search=driver.find_element(By.ID, 'search-courses')
                search.send_keys("python")
                time.sleep(4)
                driver.close()
                break

        #now i want to come to the parent handle window
        driver.switch_to.window(parent_handle)
        time.sleep(10)
        #on the pareent window handle page , i am finding webelement
        driver.find_element(By.ID, 'name').send_keys("test")
        time.sleep(3)

h=Handle()
h.window()
'''


#how to work with the frame
#frame is nothing but , suppose i have a HTML web page and i embeded another frame in the parent ,
#HTML web page
#with out switch ,we cant perform any actions on the another frame
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class switch_to_frame():
    def frame(self):
        driver = webdriver.Firefox()
        baseurl = 'https://learn.letskodeit.com/p/practice'
        driver.execute_script("window.location='https://learn.letskodeit.com/p/practice';")
        driver.maximize_window()
        driver.implicitly_wait(10)

        #using java script i can able to scroll my parent frame
        driver.execute_script("window.scrollBy(0,900);")

        #how to switch to the frame ..we have three ways like by using id,name,numbers
        #how , by using id
        driver.switch_to.frame('courses-iframe')

        #i want to work with the web elements which are on iframe
        time.sleep(10)
        driver.find_element(By.CSS_SELECTOR, '#search-courses').send_keys('python')

        #now i want to work with the parent frame
        time.sleep(5)
        driver.switch_to.default_content()
        #here i want to work with the elements which are on the parent frame
        driver.find_element(By.ID, "name").send_keys('test')


s=switch_to_frame()
s.frame()
'''

#working with the java alerts which are on the practice page
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Java_alerts():
    def alert(self):
        driver = webdriver.Firefox()
        baseurl = 'https://learn.letskodeit.com/p/practice'
        driver.execute_script("window.location='https://learn.letskodeit.com/p/practice';")
        driver.maximize_window()
        driver.implicitly_wait(10)

        #now i want to find out the Alert element
        driver.find_element(By.ID, 'name').send_keys("anil")
        driver.find_element(By.CSS_SELECTOR, '#alertbtn').click()
        time.sleep(3)
        alert1=driver.switch_to.alert
        alert1.accept()

        #now i want to work with Confirm element
        driver.find_element(By.ID, 'name').send_keys("anil")
        driver.find_element(By.CSS_SELECTOR, '#confirmbtn').click()
        time.sleep(3)
        alert2=driver.switch_to.alert
        alert2.dismiss()

j=Java_alerts()
j.alert()

'''