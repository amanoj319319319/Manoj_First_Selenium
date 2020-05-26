'''
from selenium import webdriver
class Findelement():
    def element(self):
        baseurl="https://learn.letskodeit.com/p/practice"
        driver=webdriver.Firefox()
        driver.get(baseurl)
        elementbyCLASSNAME=driver.find_element_by_class_name('cen-align')
        if elementbyCLASSNAME is not None:
            print "we found the CLASS NAME element"
        elementbyTAGNAME=driver.find_element_by_tag_name("legend")
        if elementbyTAGNAME is not None:
            print "we found the TAG NAME element"
f=Findelement()
f.element()
'''

'''
from selenium import webdriver
class Findelement():
    def element(self):
        baseurl="https://learn.letskodeit.com/p/practice"
        driver=webdriver.Firefox()
        driver.get(baseurl)
        elementbyCLASSNAME=driver.find_element_by_class_name('displayed-class')
        elementbyCLASSNAME.send_keys("testing the element")
        if elementbyCLASSNAME is not None:
            print "we found the CLASS NAME element"
        elementbyTAGNAME=driver.find_element_by_tag_name("h1")
        text=elementbyTAGNAME.text
        if elementbyTAGNAME is not None:
            print "we found the TAG NAME element:"+text
f=Findelement()
f.element()
'''

'''
from selenium import webdriver
class Findelement():
    def element(self):
        baseurl="https://learn.letskodeit.com/p/practice"
        driver=webdriver.Firefox()
        driver.get(baseurl)
        elementbyCLASSNAME=driver.find_element_by_class_name('inputs')
        elementbyCLASSNAME.send_keys("testing the element")
        if elementbyCLASSNAME is not None:s
            print "we found the CLASS NAME element"
        elementbyTAGNAME=driver.find_element_by_tag_name("h1")
        text=elementbyTAGNAME.text
        if elementbyTAGNAME is not None:
            print "we found the TAG NAME element:"+text
f=Findelement()
f.element()
'''




from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
class waitdemo():
    def wait(self):
        driver=webdriver.Firefox()
        baseurl='https://www.expedia.com'
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(10)

        driver.find_element(By.XPATH,'//*[@id="tab-flight-tab-hp"]/span[1]').click()
        driver.find_element(By.XPATH,'//*[@id="flight-origin-hp-flight"]').send_keys('Pune')
        driver.find_element(By.XPATH,'//input[@id="flight-destination-hp-flight"]').send_keys('Chennai')
        driver.find_element(By.XPATH,'//input[@id="flight-departing-hp-flight"]').send_keys('12/15/2018')
        returndate=driver.find_element(By.XPATH,'//input[@id="flight-returning-hp-flight"]')
        time.sleep(3)
        returndate.clear()
        time.sleep(3)

        returndate.send_keys('12/30/2018')
        searchbutton=driver.find_element(By.XPATH,'//*[@id="gcw-flights-form-hp-flight"]/div[7]/label')
        searchbutton.click()

        #wait=WebDriverWait(driver,10)
        #element=wait.until(EC.element_located_to_be_selected((By.ID, 'stopFilter_stops-0')))
        checkbox=WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "stopFilter_stops-0")))
        checkbox.click()




w=waitdemo()
w.wait()














