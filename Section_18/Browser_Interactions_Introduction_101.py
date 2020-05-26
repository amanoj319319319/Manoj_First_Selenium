from selenium import webdriver
driver=webdriver.Firefox()
baseurl='https://learn.letskodeit.com/p/practice'
#below method will maxmize the browser
driver.maximize_window()
#below method will open the url which you provided inside the paranthesis
driver.get(baseurl)
#below property will get the title
title=driver.title
print ("the title name is:",title)
#the below property will get the current url of the webpage
current_url=driver.current_url
print ("the current url is:",current_url)
#the below method will refresh the page
driver.refresh()
print ("browser is refreshed first time")
#the below method will also refresh the page
driver.get(driver.current_url)
print ("browser refreshed second time")
#open another url
driver.get('https://sso.teachable.com/secure/42299/users/sign_in?clean_login=true&reset_purchase_session=1')
current_url=driver.current_url
print ("the current url is:",current_url)
#browser back
driver.back()
current_url=driver.current_url
print ("the current url is after back is:",current_url)
driver.forward()
current_url=driver.current_url
print ("the current url after forword is:",current_url)
#this method will show the pagesource
pagesource=driver.page_source
print pagesource
#driver.close()..it close the current url window
#the below method will close the all the windows
driver.quit()
print ("thanks for applying all the browser interaction methods")