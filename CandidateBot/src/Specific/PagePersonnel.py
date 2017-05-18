# 
# @author David Moura <david.dbmoura at gmail.com>
# 


import Spider.BrowserOps as BO
from InformationManagement.Credentials import User
from selenium.webdriver.common.keys import Keys
import time
import subprocess

MAINURL = 'http://www.pagepersonnel.ch/'

def loginToSite():
    pass

def searchForJobs():
    BO.waitForElementLocated(browser, "edit-search-0", how='id')
    BO.waitForElementLocated(browser, "edit-location-0", how='id')
    kw = browser.find_element_by_id("edit-search-0")
    loc = browser.find_element_by_id("edit-location-0")
    kw.send_keys(search)
    loc.send_keys(location)
    loc.send_keys(Keys.RETURN)

def getJobSearchResults(browser):
    pathLocator = "//div/h2/a"
    BO.waitForElementLocated(browser, pathLocator, how='xpath')
    page_results = browser.find_elements_by_xpath(pathLocator)
    results = []
    for item in page_results:
        results.append(item)
    return results

def selectLanguage(browser, language='English'):
    BO.waitForElementLocated(browser, language, how='link')
    ele = browser.find_element_by_link_text(language)
    browser.get(ele.get_attribute('href'))

def getBlockJobs(browser, block='Technology'):
    allowed = ['Technology']
    browser.get(MAINURL)
    BO.waitForElementLocated(browser, block, how='link')
    if block in allowed:
        element = browser.find_element_by_link_text(block)
        browser.get(element.get_attribute('href'))

##NEEDS TO BE MORE ROBUST! TODO
def toggleFilters(browser):
    ID = "browse-filter-toggle"
    BO.waitForElementLocated(browser, ID)
    ele = browser.find_element_by_id(ID)
    ele.click()

def applyFilters():
    pass

    
def getJobDetails(browser): 
    refStr = getDetail(browser, "job-ref")
    reflst = [int(s) for s in refStr.split() if s.isdigit()]
    ref = reflst[0]
    details = {}
    details['jobName'] = getDetail(browser, "job-header")
    details['reference'] = ref
    details['contact'] = getDetail(browser, "field-name-field-job-consultant")
    details['location'] = getLoc(browser, "summary-detail-field")
    print(getDetail(browser, "field-name-field-job-location-txt"))
    details['company'] = getDetail(browser, "field-name-field-job-desc-company")
    details['description'] = getDetail(browser, "field-name-field-job-desc-role")
    details['site'] = 'PagePersonnel'
    details['type'] = getContractType(browser, "summary-detail-field")
    print(getDetail(browser, "field-name-field-job-contract-type"))
    return details
    
def getDetail(browser, identifier):
    BO.waitForElementLocated(browser, identifier, how='class')
    ele = browser.find_element_by_class_name(identifier)
    return ele.text

def getLoc(browser, identifier):
    BO.waitForElementLocated(browser, identifier, how='class')
    elements = browser.find_elements_by_class_name(identifier)
    for element in elements:
        ele = element.find_element_by_xpath('.//span[@class = "summary-detail-field-label"]')
        if ele.text == 'Location:':
            el = element.find_element_by_xpath('.//span[@class = "summary-detail-field-value"]')
            return el.text

def getContractType(browser, identifier):
    BO.waitForElementLocated(browser, identifier, how='class')
    elements = browser.find_elements_by_class_name(identifier)
    for element in elements:
        ele = element.find_element_by_xpath('.//span[@class = "summary-detail-field-label"]')
        if ele.text == 'Contract Type:':
            el = element.find_element_by_xpath('.//span[@class = "summary-detail-field-value"]')
            return el.text


def loginLinkedIn(browser, us):
    BO.waitForElementLocated(browser, "session_key-oauth2SAuthorizeForm")
    credentials = us.getAppCredentials('LinkedIn')
    elements = ("session_key-oauth2SAuthorizeForm", "session_password-oauth2SAuthorizeForm")
    BO.login(browser, elements, credentials)

def applyThroughLinkedIn(browser, us):
    BO.waitForElementLocated(browser, 'linkedin-form-apply', how='class')
    ele = browser.find_element_by_class_name('linkedin-form-apply')
    BO.waitForElementLocated(browser, 'a', how='tag')
    el = ele.find_element_by_tag_name('a')
    browser.get(el.get_attribute('href'))
    loginLinkedIn(browser, us)
    BO.waitForElementLocated(browser, "edit-telephone")
    tel = browser.find_element_by_id('edit-telephone')
    tel.send_keys(us.personal['telephone'])
    browser.execute_script("document.getElementById('edit-privacy-data-2').click();")
    browser.execute_script("document.getElementById('edit-submit').click();")

def applyThroughCV(browser, us):
    BO.waitForElementLocated(browser, 'apply-with-cv-link', how='id')
    browser.execute_script("document.getElementById('apply-with-cv-link').click();")
    fn = browser.find_element_by_id('edit-firstname')
    ln = browser.find_element_by_id('edit-lastname')
    tp = browser.find_element_by_id('edit-telephone')
    email = browser.find_element_by_id('edit-email')
    fn.send_keys(us.personal['firstName'])
    ln.send_keys(us.personal['lastName'])
    tp.send_keys(us.personal['telephone'])
    email.send_keys(us.personal['email'])
    browser.find_element_by_id('edit-field-3rd-party-file-upload-und-0').send_keys(us.personal['CVPath'])#works!
    browser.execute_script("document.getElementsByClassName('option')[0].click();")
    time.sleep(3)
    browser.execute_script("document.getElementById('edit-submit').click();")
    #DONE
    
def applyToJob(browser, us, linkedIn=False):
    browser.execute_script("document.getElementsByClassName('apply-job')[0].click();")
    if linkedIn:
        applyThroughLinkedIn(browser, us)
    else:
        applyThroughCV(browser, us)

browser = BO.openNewBrowser(MAINURL)
getBlockJobs(browser, 'Technology')
toggleFilters(browser)
selectLanguage(browser)
res = getJobSearchResults(browser)

links = BO.getLinksFromElements(res)
us = User('f')
browser.get( url=links[0])
applyToJob(browser, us)
#dets = getJobDetails(browser)

#for d in dets.items():
#    print(d)

print('done')
    
    