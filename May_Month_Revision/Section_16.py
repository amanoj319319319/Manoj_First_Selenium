from selenium import webdriver
import os
import time

class ietests(object):
    def ie(self):
        driverlocation=("C:\\Users\\Manoj\\Desktop\\MANOJ SORT APPLICATIONS\\IEDriverServer_x64_3.14.0\\IEDriverServer.exe")
        os.environ["webdriver.ie.driver"] = driverlocation
        driver=webdriver.Ie(driverlocation)
        driver.get("https://www.flipkart.com")
        time.sleep(5)
        driver.close()
ii=ietests()
ii.ie()
