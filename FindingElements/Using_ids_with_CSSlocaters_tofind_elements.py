'''
from selenium import webdriver
import time
driver=webdriver.Firefox()
url="https://en-gb.facebook.com/login/"
driver.get(url)
username=eval(raw_input("enter your username:"))
password=eval(raw_input("enter your password:"))
elementbyid=driver.find_element_by_id("email")
elementbyid.send_keys(username)
elementbyide=driver.find_element_by_id("pass")
elementbyide.send_keys(password)
elementbyidee=driver.find_element_by_id("loginbutton")
elementbyidee.click()
time.sleep(15)
'''
#Tutor explained only these things on this class
#tutor explained how to find multiple CSS-Ids on a web page.
'''
syntax:
1)tag[attribute='value']
2)'#'..Id
3)'.'..Class
'''
#diff ways of matching elements or nodes are..nothing but , how to check the elements of web page are sharing ,
#the same Id ...on mac os i saw , on windows i have to check with experts.

#Element displayed example text box
'''
1)input[id='displayed-text']
2)#displayed-text
3)input#displayed-text
'''