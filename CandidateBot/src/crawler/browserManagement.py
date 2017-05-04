# 
# @author David Moura <david.dbmoura at gmail.com>
# 


import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

windowsNames = {}

def openNewBrowser(url='http://www.google.com'):
    chromepath = "C:/Users/David/Desktop/RandomPessoal/Software/chromedriver_win32/chromedriver.exe"
    browser = webdriver.Chrome(chromepath)
    browser.get(url)
    return browser

def openNewTab(url='http://www.google.com', name=None):
    browser.execute_script("window.open(%s, 'new_window')"%url)
    if name != None:
        windowsNames[name] = browser.current_window_handle

def changeWindow(browser, name):
    if name in windowsNames:
        browser.switch_to.window(windowsNames[name])
    else:
        raise NameError('Not valid name')

def seleniumGoogleSearch(browser, searchTerm):
    search = browser.find_element_by_name('q')
    search.send_keys(searchTerm)
    search.send_keys(Keys.RETURN)

browser = openNewBrowser()
seleniumGoogleSearch(browser,"david")
time.sleep(3)
browser.quit()