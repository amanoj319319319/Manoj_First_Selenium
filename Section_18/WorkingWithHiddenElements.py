from selenium import  webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Firefox()
'''
baseurl='https://learn.letskodeit.com/p/practice'
driver.get(baseurl)
driver.implicitly_wait(6)

#Find the state of the text box
textboxelement=driver.find_element_by_id('displayed-text')
textboxstate=textboxelement.is_displayed()#True if visible..False if it is hidden
#Exception if not present in the dom
print ("Text is visible?",textboxstate)
time.sleep(5)

#click the hide button
hide=driver.find_element_by_id('hide-textbox')
hide.click()
#when it is hided,what is the result
#Find the state of the text box
textboxstate=textboxelement.is_displayed()
print ("Text is visible?",textboxstate)
time.sleep(5)

#click the show button
show=driver.find_element_by_id('show-textbox')
show.click()
time.sleep(5)
#when it clicked the show button,what is the result
#find the state of the box
textboxstate=textboxelement.is_displayed()
print ("Text is visible?",textboxstate)
time.sleep(5)

'''


baseurl='https://www.expedia.com/'
driver.maximize_window()
driver.get(baseurl)
driver.implicitly_wait(3)

driver.find_element_by_xpath('tab-flight-tab').click()

dropdownelement=driver.find_element_by_xpath('flight-age-select-1')
print ('element is visible?',dropdownelement)
