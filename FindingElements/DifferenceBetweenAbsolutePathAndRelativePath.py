'''
#Syntax of XPATH..
//Tag[@attribute="value"]
Diff between single slash and double slash.
single slash gives an immediate child in the parent element
example of single and double slash
ex:=  //*[@id="block-1069048"]/div/div/div/div[5]
double slash gives an immediate and nested childs also in the parent element
Absolute path and Relative path

//*[@id="block-1069048"]/div/div/div/div[5]


how to build an effective XPATH:-
---------------------------------
//div[@id="navbar"]//ul/li/[2]/a..:
    syntax:--  //Tag[@atrribute="value]//chilldelement/childelement/
when ever we use // slash after this Tag[@atrribute="value] ,it will find the childelement ,
where ever present under this attribute.
***********************************************************************************
beautiful example of effective XPATH on tutors practice page:
i inspected practice page table.
//*[@id="product"]/tbody/tr[2]/td[1]
//*[@id="product"]//td[1]...............Effective XPATH
'''


from selenium import webdriver
from selenium.webdriver.common.by import By
import time
baseurl='https://www.google.com/'
driver=webdriver.Firefox()
driver.get(baseurl)
driver.implicitly_wait(30)
element=driver.find_element(By.ID,'combobo')
element.submit()








