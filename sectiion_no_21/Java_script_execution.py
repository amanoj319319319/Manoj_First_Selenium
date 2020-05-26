#it is working in our windows
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class JavaScriptExecution():

    def test(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        # driver.get("https://letskodeit.teachable.com/pages/practice")
        driver.execute_script("window.location = 'https://letskodeit.teachable.com/pages/practice';")
        driver.implicitly_wait(3)
        time.sleep(12)

        # element = driver.find_element(By.ID, "name")
        element = driver.execute_script("return document.getElementById('name');")
        element.send_keys("Test")

ff = JavaScriptExecution()
ff.test()


#how to get the size of the window

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class windowsize():
    def window(self):
        driver = webdriver.Firefox()
        baseurl='https://learn.letskodeit.com/p/practice'
        driver.maximize_window()
        driver.implicitly_wait(10)

        height=driver.execute_script("return window.innerHeight")
        width=driver.execute_script("return window.innerWidth")

        print ("height of the window is :",height)
        print ("width of the window is :",width)

        driver.quit()
ww=windowsize()
ww.window()


#how to scroll element in to view

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ScrollingElement():

    def test(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get("https://letskodeit.teachable.com/pages/practice")
        driver.implicitly_wait(3)


        # Scroll Down
        driver.execute_script("window.scrollBy(0, 1000);")
        time.sleep(3)

        # Scroll Up
        driver.execute_script("window.scrollBy(0, -1000);")
        time.sleep(3)

        # Scroll Element Into View
        element = driver.find_element(By.ID, "mousehover")
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(2)
        driver.execute_script("window.scrollBy(0, -150);")

        # Native Way To Scroll Element Into View
        time.sleep(2)
        driver.execute_script("window.scrollBy(0, -1000);")
        location = element.location_once_scrolled_into_view
        print("Location: " + str(location))
        driver.execute_script("window.scrollBy(0, -150);")



ff = ScrollingElement()
ff.test()

'''