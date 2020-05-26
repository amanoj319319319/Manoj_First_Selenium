#How to work with mouse hover elements on the page
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

class MouseHover():
    def mouse(self):
        driver = webdriver.Firefox()
        baseurl = 'https://learn.letskodeit.com/p/practice'
        #driver.execute_script("window.location='https://learn.letskodeit.com/p/practice';")
        driver.get(baseurl)
        driver.maximize_window()
        driver.implicitly_wait(10)

        #using java script i can able to scroll down the page down
        driver.execute_script("window.scrollBy(0,900);")


        #first i need to find the Mouse Hover element which is on practice page
        time.sleep(10)
        element=driver.find_element(By.ID, "mousehover")
        actions=ActionChains(driver)

        actions.move_to_element(element).perform()
        time.sleep(4)

        #i am finding the path for Top link which is in Mouse Hover
        Top_link='//*[@id="block-1069048"]/div/div/div/div[4]/div/fieldset/div/div/a[1]'
        Top=driver.find_element(By.XPATH, Top_link)
        actions.move_to_element(Top).click().perform()
        print ("webdriver clcked the Top link")
        time.sleep(10)

        element = driver.find_element(By.ID, "mousehover")
        actions.move_to_element(element).perform()
        time.sleep(4)

        #i am finding the path for the Reload link also
        Reload_link='#block-1069048 > div > div > div > div:nth-child(7) > div > fieldset > div > div > a:nth-child(2)'
        Reload=driver.find_element(By.CSS_SELECTOR, Reload_link)
        actions.move_to_element(Reload).click().perform()
        print ("webdriver clcked on the reload link")

m=MouseHover()
m.mouse()
'''


#working with the drop and down
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

class Drag_and_Drop():
    def drag(self):
        driver = webdriver.Firefox()
        baseurl = 'https://jqueryui.com/droppable/'
        # driver.execute_script("window.location='https://learn.letskodeit.com/p/practice';")
        driver.get(baseurl)
        driver.maximize_window()
        driver.implicitly_wait(10)

        driver.switch_to.frame(0)
        time.sleep(10)
        drag_id=driver.find_element(By.ID, "draggable")
        drop_id=driver.find_element(By.ID, "droppable")
        time.sleep(10)
        actions = ActionChains(driver)
        actions.drag_and_drop(drag_id, drop_id).perform()
        print ("it dragged the element and then it dropped in the target")
d=Drag_and_Drop()
d.drag()
'''

#how to work with the sliders
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

class sliders():
    def slider(self):
        driver = webdriver.Firefox()
        baseurl = 'https://jqueryui.com/slider/'
        # driver.execute_script("window.location='https://learn.letskodeit.com/p/practice';")
        driver.get(baseurl)
        driver.maximize_window()
        driver.implicitly_wait(10)

        actions=ActionChains(driver)

        driver.switch_to.frame(0)
        time.sleep(10)
        slider=driver.find_element(By.CSS_SELECTOR, '#slider > span')
        actions.drag_and_drop_by_offset(slider,100,0).perform()
        print ("the slider has been dragged upto 100 pixels")

s=sliders()
s.slider()
'''

