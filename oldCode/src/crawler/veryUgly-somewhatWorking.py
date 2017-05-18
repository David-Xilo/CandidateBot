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
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from selenium.webdriver.common.action_chains import ActionChains

from bs4 import BeautifulSoup
from urllib.request import urlopen

MAINURL = 'http://www.pagepersonnel.ch/'


def doJobSearch(browser, search, location):
    searchElementID = "edit-search-0"
    locationElementID = "edit-location-0"
    kw = browser.find_element_by_id(searchElementID)
    loc = browser.find_element_by_id(locationElementID)
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
    WebDriverWait(browser, 30).until( EC.element_to_be_clickable( (By.ID, ID) ) )
    ele = browser.find_element_by_id(ID)
    ele.click()
    
def getJobsApplicationURL(htmlSoup):            
    #page = response.read()  
    soup = BeautifulSoup(htmlSoup, "xml")
    print(soup.prettify())		
    #jobs = soup.find('a', {'class' : 'jquery-once-1-processed'})
    jobs = soup.find_all('a', {'class' : 'jquery-once-1-processed'})
    return jobs

browser = browserManagement.openNewBrowser(MAINURL)

def applyToJob(browser, windowName = "", linkedIn = False):
    browser.execute_script("document.getElementsByClassName('apply-job')[0].click();")
    #TODO

getAllBlockJobs(browser, 'Technology')
toggleFilters(browser)
selectEnglishLanguage(browser)
res = getJobSearchResults(browser)
links = getLinksFromResults(res)
#browserManagement.openNewTab(browser, url=links[0], name='test')
browserManagement.getPage(browser, url=links[0])
WebDriverWait(browser, 30).until( EC.element_to_be_clickable( (By.CLASS_NAME, 'container') ) )
#tst = browser.find_element_by_id('content-area') ## THIS WORKS FOR THE DETAILS!
body = browser.find_element_by_id('page')
soup = BeautifulSoup(browser.page_source, "xml")
print(soup.prettify())
tst = browser.find_element_by_id('content-area')#class_name('container')
print(tst)
ts = tst.find_element_by_class_name('item-list')
print(ts)
t = ts.find_element_by_class_name('first')
print(t)
ap = t.find_elements_by_tag_name('a')
print(ap[0].get_attribute('href'))
browser.execute_script("document.getElementsByClassName('apply-job')[0].click();")

#browser.switch_to.frame(browser.find_element_by_tag_name("iframe"))
#print(browser.page_source)
#browser.switch_to.frame(browser.find_element_by_tag_name("iframe"))
#print(browser.page_source)
#browser.execute_script("$(arguments[0]).click();", ap)
#print(tst.get_attribute('innerHTML'))#### VERY IMPORTANT, THE HTML I NEED
#jobs = getJobsApplicationURL(tst.get_attribute('outerHTML'))
#print(tst.get_attribute('innerHTML'))
#for j in jobs:
#    print(j.get('href'))

#browserManagement.getPage(browser, url= (MAINURL + jobs[0].get('href')))
#i = tst.find_element_by_tag_name('ul')
#ts = i.find_element_by_tag_name('a')

#print(ts.get_attribute('innerHTML'))
#print(i.get_attribute('innerHTML'))

time.sleep(4)
#browser.quit()
print('done')

main_window_handle = browser.current_window_handle
browser.execute_script("document.getElementsByClassName('google-picker')[0].click();")
    signin_window_handle = None
    
    while not signin_window_handle:
        for handle in browser.window_handles:
            if handle != main_window_handle:
                signin_window_handle = handle
                break
    browser.switch_to.window(signin_window_handle)
    un = browser.find_element_by_id('identifierId')
    un.send_keys(us.username['GMail'])
    #WebElement.sendKeys(Keys.RETURN)
    un.send_keys(Keys.RETURN)
    time.sleep(3)
    pw = browser.find_element_by_class_name('whsOnd')
    pw.send_keys(us.password['GMail'])
    pw.send_keys(Keys.RETURN)
    time.sleep(3)
    browser.execute_script("document.getElementsByClassName('RveJvd')[0].click();")