# 
# @author David Moura <david.dbmoura at gmail.com>
# 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


def openNewBrowser(url='http://www.google.com/'):
    chromepath = "C:/Users/David/Desktop/RandomPessoal/Software/chromedriver_win32/chromedriver.exe"
    browser = webdriver.Chrome(chromepath)
    browser.get(url)
    return browser

def goBack(browser):
    browser.execute_script("window.history.go(-1)")
    
def openNewTab(browser, url='http://www.google.com', name=None):
    command = "window.open(" + "'" + url + "'" + ", 'new_window')"
    browser.execute_script(command)
    if name != None:
        windowsNames[name] = browser.current_window_handle
        
def changeTab(browser, name):
    if name in windowsNames:
        browser.switch_to.window(windowsNames[name])
    else:
        raise NameError('Not valid name')

def waitForElementLocated(browser, identifier, how='id', delay = 30):
    if how == 'link':
        WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.LINK_TEXT, identifier)))
    elif how == 'id':
        WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, identifier)))
    elif how == 'xpath':
        WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, identifier)))
    elif how == 'class':
        WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CLASS_NAME, identifier)))
    elif how == 'name':
        WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.NAME, identifier)))
    elif how == 'tag':
        WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.TAG_NAME, identifier)))
    else:
        raise NameError('invalid manner')

def login(browser, elements, cred):
    username = browser.find_element_by_id(elements[0])
    username.send_keys(cred[0])
    password = browser.find_element_by_id(elements[1])
    password.send_keys(cred[1])
    password.submit()
    

def getLinksFromElements(elements):
    links = []
    for it in elements:
        links.append(it.get_attribute('href'))
    return links

def isElementPresent(browser, locator, how='class'):
    try:
        if how == 'class':
            browser.find_element_by_class_name(locator)
        elif how == 'link':
            browser.find_element_by_link_text(locator)
        elif how == 'id':
            browser.find_element_by_id(locator)
        else:
            print('bad call at "isElementPresent"')
            raise NoSuchElementException
    except NoSuchElementException:
        return False
    return True