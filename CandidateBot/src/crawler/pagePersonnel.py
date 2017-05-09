# 
# @author David Moura <david.dbmoura at gmail.com>
# 

import browserManagement
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import action_chains, keys
from selenium.webdriver.common.action_chains import ActionChains

MAINURL = 'http://www.pagepersonnel.ch/'


def doJobSearch(browser, search, location):
    searchElementID = "edit-search-0"
    locationElementID = "edit-location-0"
    kw = browserManagement.searchElementByID(browser, searchElementID)
    loc = browserManagement.searchElementByID(browser, locationElementID)
    kw.send_keys(search)
    loc.send_keys(location)
    loc.send_keys(Keys.RETURN)

def getJobSearchResults(browser):
    pathLocator = "//div/h2/a"
    page_results = browser.find_elements(By.XPATH, pathLocator)
    results = []
    for item in page_results:
        results.append(item)
    return results

def getLinksFromResults(results):
    links = []
    for it in results:
        links.append(it.get_attribute('href'))
    return links

def getAllBlockJobs(browser, block):
    browserManagement.getPage(browser, MAINURL)
    element = browser.find_element_by_link_text(block)
    browserManagement.getPage(browser, element.get_attribute('href'))
    
def selectEnglishLanguage(browser):
    ele = browser.find_element_by_link_text('English')
    browserManagement.getPage(browser, ele.get_attribute('href'))

def toggleFilters(browser):
    ID = "browse-filter-toggle"
    ele = browser.find_element_by_id(ID)
    ele.click()
    

browser = browserManagement.openNewBrowser(MAINURL)

def applyToJob(browser, windowName = "", linkedIn = False):
    browser.execute_script("document.getElementsByClassName('apply-job')[0].click();")
    #TODO

doJobSearch(browser, "junior", "lausanne")
res = getJobSearchResults(browser)
links = getLinksFromResults(res)
browserManagement.getPage(browser, links[0])


getAllBlockJobs(browser, 'Technology')
toggleFilters(browser)
selectEnglishLanguage(browser)
res = getJobSearchResults(browser)
links = getLinksFromResults(res)
browserManagement.openNewTab(browser, url=links[0], name='test')


