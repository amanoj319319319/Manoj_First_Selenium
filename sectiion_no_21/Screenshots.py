'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Screenshots(object):
    def screenshot(self):
       driver=webdriver.Firefox()
       baseurl='https://learn.letskodeit.com/p/practice'
       driver.maximize_window()
       driver.get(baseurl)
       driver.implicitly_wait(10)

       Login_link=driver.find_element(By.LINK_TEXT, 'Login')
       Login_link.click()

       Email_box=driver.find_element(By.CSS_SELECTOR, '#user_email')
       Email_box.send_keys('a.manoj20@gmail.com')

       Password_box=driver.find_element(By.CSS_SELECTOR, '#user_password')
       Password_box.send_keys('manoj')

       Log_in_button=driver.find_element(By.CSS_SELECTOR ,'#new_user > div.form-group.text-center > input')
       Log_in_button.click()

       Screenshot_save_location="C:\\Users\\Manoj\\Desktop\\login.png"
       #login is file name and .png is extemsion of this file

       try:
           driver.save_screenshot(Screenshot_save_location)
           print "your screen shot is saved"
       except Exception as e:
           print e

ss=Screenshots()
ss.screenshot()
'''

#generic method of taking screen shots


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Screenshots(object):
    def takescreenshot(self, driver):
        '''this method take screenshots of current open web page , parameter is driver ,return '''
        filename = str(round(time.time() * 1000)) + ".png"
        screenshotdirectory = "C:\\Users\\Manoj\\Desktop\\"+filename
        #destinationfilename = screenshotdirectory + filename
        try:
            driver.save_screenshot(screenshotdirectory)
            print "your screen shot is saved"
        except Exception as e:
            print "your screen shot is not saved"

    def screenshot(self):
       driver=webdriver.Firefox()
       baseurl='https://learn.letskodeit.com/p/practice'
       driver.maximize_window()
       driver.get(baseurl)
       driver.implicitly_wait(10)

       Login_link=driver.find_element(By.LINK_TEXT, 'Login')
       Login_link.click()

       Email_box=driver.find_element(By.CSS_SELECTOR, '#user_email')
       Email_box.send_keys('a.manoj20@gmail.com')

       Password_box=driver.find_element(By.CSS_SELECTOR, '#user_password')
       Password_box.send_keys('manoj')

       Log_in_button=driver.find_element(By.CSS_SELECTOR ,'#new_user > div.form-group.text-center > input')
       Log_in_button.click()
       self.takescreenshot(driver)


ss=Screenshots()
ss.screenshot()
