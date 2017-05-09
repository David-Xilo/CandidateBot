# 
# @author David Moura <david.dbmoura at gmail.com>
# 


import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


windowsNames = {}

def getPage(browser, url):
    browser.get(url)

def goBack(browser):
    browser.execute_script("window.history.go(-1)")

def openNewBrowser(url='http://www.google.com/'):
    chromepath = "C:/Users/David/Desktop/RandomPessoal/Software/chromedriver_win32/chromedriver.exe"
    browser = webdriver.Chrome(chromepath)
    browser.get(url)
    return browser

def openNewTab(browser, url='http://www.google.com', name=None):
    command = "window.open(" + "'" + url + "'" + ", 'new_window')"
    browser.execute_script(command)
    if name != None:
        windowsNames[name] = browser.current_window_handle

def changeWindow(browser, name):
    if name in windowsNames:
        browser.switch_to.window(windowsNames[name])
    else:
        raise NameError('Not valid name')

def searchElementByXPath(browser, path):
    return WebDriverWait(browser, 120).until(EC.visibility_of_element_located((By.XPATH, path)))

#def searchElementByID(browser, ID):
#    return WebDriverWait(browser, 120).until( EC.element_to_be_clickable( (By.ID, ID) ) )

def login(browser, elements, cred):
    username = browser.find_element_by_id(elements[0])
    username.send_keys(cred[0])
    password = browser.find_element_by_id(elements[1])
    password.send_keys(cred[1])
    password.submit()


#browser = openNewBrowser()
#seleniumGoogleSearch(browser,"david")
#openNewTab(browser)
#time.sleep(3)
#browser.quit()