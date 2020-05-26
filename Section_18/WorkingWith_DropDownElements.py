from selenium import webdriver
#from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
driver=webdriver.Firefox()
'''
baseurl='https://learn.letskodeit.com/p/practice'
driver.get(baseurl)
driver.implicitly_wait(5)

element=driver.find_element_by_id("carselect")
sel=Select(element)

sel.select_by_value('benz')
print "select by value"
time.sleep(3)

sel.select_by_index(2)
print "select by index"
time.sleep(3)

sel.select_by_visible_text('BMW')
print "select by visible text"
time.sleep(3)

sel.select_by_index(2)
print "select by index"

#we should import this #from selenium.webdriver.common.by import By in this dropdown case.
#if i imported this one ,i was getting an error.
'''
baseurl='https://www.redbus.in/hotels/'
driver.get(baseurl)
#for span type dropdowns we should do like this
#ex:-<span class="icon icon-right dropDown"></span>
#for span type dropdowns Select wont works
manage=driver.find_element_by_xpath("//span[text()='Manage Booking']")
manage.click()
cancel=driver.find_element_by_xpath("//a[@title='Cancel Your Ticket']")
cancel.click()