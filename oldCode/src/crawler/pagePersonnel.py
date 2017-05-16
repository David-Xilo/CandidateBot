# 
# @author David Moura <david.dbmoura at gmail.com>
# 

import browserManagement as BM
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import action_chains, keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from linkedInCrawler import loginLinkedIn

from selenium.webdriver.common.action_chains import ActionChains
from im.credentialManager import Me
from bs4 import BeautifulSoup
from urllib.request import urlopen

MAINURL = 'http://www.pagepersonnel.ch/'


def doJobSearch(browser, search, location):
    searchElementID = "edit-search-0"
    locationElementID = "edit-location-0"
    BM.waitForElementLocated(browser, 'id', searchElementID)
    BM.waitForElementLocated(browser, 'id', locationElementID)
    kw = browser.find_element_by_id(searchElementID)
    loc = browser.find_element_by_id(locationElementID)
    kw.send_keys(search)
    loc.send_keys(location)
    loc.send_keys(Keys.RETURN)

def getJobSearchResults(browser):
    pathLocator = "//div/h2/a"
    BM.waitForElementLocated(browser, 'xpath', pathLocator)
    page_results = browser.find_elements(By.XPATH, pathLocator)
    results = []
    for item in page_results:
        results.append(item)
    return results

def createLinkDict(htmlElements):
    result = {}
    for ele in htmlElements:
        key = ele.get_attribute('text')
        value = ele.get_attribute('href')
        result[key] = value
    return result

def getAllBlockJobs(browser, block, delay = 30):
    BM.getPage(browser, MAINURL)
    BM.waitForElementLocated(browser, 'link', block)
    element = browser.find_element_by_link_text(block)
    BM.getPage(browser, element.get_attribute('href'))
    
def selectEnglishLanguage(browser):
    BM.waitForElementLocated(browser, 'link', 'English')
    ele = browser.find_element_by_link_text('English')
    BM.getPage(browser, ele.get_attribute('href'))

##NEEDS TO BE MORE ROBUST! TODO
def toggleFilters(browser):
    ID = "browse-filter-toggle"
    BM.waitForElementClickable(browser, 'id', ID)
    ele = browser.find_element_by_id(ID)
    ele.click()

def applyToJob(browser, windowName = "", linkedIn = False):
    if windowName:
        #changes conntext to window
        BM.changeWindow(browser, windowName)
    browser.execute_script("document.getElementsByClassName('apply-job')[0].click();")
    ele = browser.find_element_by_class_name('linkedin-form-apply')
    el = ele.find_element_by_tag_name('a')
    BM.getPage(browser, el.get_attribute('href'))
    loginLinkedIn(browser)
    BM.waitForElementLocated(browser, 'id', "edit-telephone")
    tel = browser.find_element_by_id('edit-telephone')
    tel.send_keys('764683355')
    #check = browser.find_element_by_id('edit-privacy-data-2')
    browser.execute_script("document.getElementById('edit-privacy-data-2').click();")
    browser.execute_script("document.getElementById('edit-submit').click();")
    #browser.execute_script("document.getElementsByClassName('linkedin-form-apply')[0].click();")
    #browser.execute_script("document.getElementById('apply-with-cv-link').click();")
    #browser.execute_script("document.getElementById('edit-firstname').click();")
    #fn = browser.find_element_by_id('edit-firstname')
    #fn.send_keys('David')
    #ln = browser.find_element_by_id('edit-lastname')
    #ln.send_keys('Moura')
    #telephone = browser.find_element_by_id('edit-telephone')
    #telephone.send_keys('764683355')
    #email = browser.find_element_by_id('edit-email')
    #email.send_keys('david.dbmoura@gmail.com')
    #email.send_keys(Keys.RETURN)
    #print(ele)
    #TODO

browser = BM.openNewBrowser(MAINURL)
getAllBlockJobs(browser, 'Technology')
toggleFilters(browser)
selectEnglishLanguage(browser)
res = getJobSearchResults(browser)
#jobs = createLinkDict(res)
links = BM.getLinksFromElements(res)
#print(links)
#for l, k in links.items():
#    print(l , k)
#browserManagement.openNewTab(browser, url=links[0], name='test')
BM.getPage(browser, url=links[0])
applyToJob(browser)

#time.sleep(4)
#browser.quit()
print('done')