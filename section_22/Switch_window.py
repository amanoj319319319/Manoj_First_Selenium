'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class switch_window():
    def switch(self):
        driver=webdriver.Firefox()
        baseurl='https://learn.letskodeit.com/p/practice'
        driver.maximize_window()
        driver.get(baseurl)

        #find parent handle ie main window
        parent_handle=driver.current_window_handle
        print ("The current window handle is :",parent_handle)

        #find open window button and click it
        driver.find_element(By.ID, "openwindow").click()

        #find all handles ,there are two handles will come after clicking the open window button
        handles=driver.window_handles

        #switch to window and search course
        for handle in handles:
            print handle

ss=switch_window()
ss.switch()

'''


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class switch_window():
    def switch(self):
        driver=webdriver.Firefox()
        baseurl='https://learn.letskodeit.com/p/practice'
        driver.maximize_window()
        driver.get(baseurl)

        #find parent handle ie main window
        parent_handle=driver.current_window_handle
        print ("The current window handle is :",parent_handle)

        #find open window button and click it
        driver.find_element(By.ID, "openwindow").click()

        #find all handles ,there are two handles will come after clicking the open window button
        handles=driver.window_handles

        #switch to window and search course
        for handle in handles:
            print handle
            if handle not in parent_handle:
                driver.switch_to.window(handle)
                print ("switched to window like :",handle)
                time.sleep(15)
                driver.find_element(By.ID, "search-courses").send_keys("python")
                time.sleep(3)
                driver.close()
                break

        #switch back to parent handle
        driver.switch_to.window(parent_handle)
        driver.find_element(By.ID, "name").send_keys("test")

ss=switch_window()
ss.switch()

ss=switch_window()
ss.switch()
