#working with mouse hover elements which are on the practice page
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

class Mouse_Hover():
    def mouse(self):
        driver = webdriver.Firefox()
        baseurl = 'https://learn.letskodeit.com/p/practice'
        driver.get(baseurl)
        driver.maximize_window()
        driver.implicitly_wait(10)


        driver.execute_script("window.scrollBy(0,800);")
        time.sleep(3)

        mouse_hover=driver.find_element(By.ID, "mousehover")
        actions = ActionChains(driver)
        actions.move_to_element(mouse_hover).perform()
        print "webdriver has clicked on the mouse hover button"


        time.sleep(3)
        Top=driver.find_element(By.CSS_SELECTOR,
                                '#block-1069048 > div > div > div > div:nth-child(7) > div > fieldset > div > div > a:nth-child(1)')
        actions.move_to_element(Top).click().perform()
        print "web driver has clicked on the Top link"
        time.sleep(10)

        #actions = ActionChains(driver)
        element = driver.find_element(By.ID, "mousehover")
        actions.move_to_element(element).perform()
        time.sleep(4)

        # i am finding the path for the Reload link also
        Reload_link = '#block-1069048 > div > div > div > div:nth-child(7) > div > fieldset > div > div > a:nth-child(2)'
        Reload = driver.find_element(By.CSS_SELECTOR, Reload_link)
        actions.move_to_element(Reload).click().perform()
        print ("webdriver clcked on the reload link")


m=Mouse_Hover()
m.mouse()

'''

#WORKING WITH DRAG AND DROPS
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

class Mouse_Hover():
    def mouse(self):
        driver = webdriver.Firefox()
        baseurl = 'https://jqueryui.com/droppable/'
        driver.get(baseurl)
        driver.maximize_window()
        driver.implicitly_wait(10)

        actions=ActionChains(driver)

        driver.switch_to.frame(0)
        time.sleep(10)
        draggable=driver.find_element(By.ID, "draggable")
        droppable=driver.find_element(By.ID, "droppable")

        time.sleep(5)
        actions.drag_and_drop(draggable,droppable).perform()
m=Mouse_Hover()
m.mouse()
'''

#HOW TO WORK WITH THE SLIDERS
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

class Sliders():
    def slider(self):
        driver = webdriver.Firefox()
        baseurl = 'https://jqueryui.com/slider/'
        driver.get(baseurl)
        driver.maximize_window()
        driver.implicitly_wait(10)

        actions=ActionChains(driver)

        driver.switch_to.frame(0)
        time.sleep(10)
        slider=driver.find_element(By.CSS_SELECTOR, "#slider > span")
        actions.drag_and_drop_by_offset(slider,100,0).perform()
        time.sleep(3)
s=Sliders()
s.slider()
'''







