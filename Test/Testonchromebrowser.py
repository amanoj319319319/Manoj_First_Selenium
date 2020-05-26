'''
from selenium import webdriver
import os
class Runtestonwindows(object):
    def chrome(self):
        driverlocation="C:\\Users\\Manoj\\Desktop\\MANOJ SORT APPLICATIONS\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"]=driverlocation
        driver=webdriver.Chrome(driverlocation)
        driver.get("https://www.youtube.com/results?search_query=yemi+sodara+song")
r=Runtestonwindows()
r.chrome()
'''
'''
from selenium import webdriver
import os,time
def chrome():
    driverlocation = "C:\\Users\\Manoj\\Desktop\\MANOJ SORT APPLICATIONS\\chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = driverlocation
    driver = webdriver.Chrome(driverlocation)
    driver.get("https://www.youtube.com/results?search_query=yemi+sodara+song")
    time.sleep(15)
    driver.quit()
chrome()
'''

#Running test on internet explorer
'''
from selenium import webdriver
import os,time
def iedriver():
    driverlocation = "C:\\Users\\Manoj\\Desktop\\MANOJ SORT APPLICATIONS\\IEDriverServer.exe"
    os.environ["webdriver.ie.driver"] = driverlocation
    driver = webdriver.Ie(driverlocation)
    driver.get("https://www.youtube.com/results?search_query=yemi+sodara+song")
    time.sleep(15)
    driver.quit()
iedriver()
'''