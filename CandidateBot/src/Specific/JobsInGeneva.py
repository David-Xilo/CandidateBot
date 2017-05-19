# 
# @author David Moura <david.dbmoura at gmail.com>
# 


import Spider.BrowserOps as BO
from InformationManagement.Credentials import User
from selenium.webdriver.common.keys import Keys
import time
import InformationManagement.DataLog as DL
import os

MAINURL = 'http://www.jobsingeneva.com/jobs/IT%20Technology'


def getJobSearchResults(browser):
    firstLocator = "jobs"
    BO.waitForElementLocated(browser, firstLocator, how='class')
    superElement = browser.find_element_by_class_name(firstLocator)
    locator = "job-link"
    BO.waitForElementLocated(browser, locator, how='class')
    page_results = superElement.find_elements_by_class_name(locator)
    results = []
    for item in page_results:
        results.append(item)
    return results
    
    
def getJobDetails(browser):
    details = {}
    BO.waitForElementLocated(browser, 'searchContainer', how='class')
    masterElement = browser.find_element_by_class_name('searchContainer')
    name = masterElement.find_element_by_class_name("searchTitle")
    details['jobName'] = name.text
    #there are 2 search specifics:
    #1st contains company - 0 and location - 1
    #2nd contains reference - 3, contact - 1 and type - 0 (2 is date of publication)
    BO.waitForElementLocated(browser, 'searchSpecifics', how='class')
    elements = masterElement.find_elements_by_class_name('searchSpecifics')
    details['reference'] = getDetail(elements[1], 'Referencia')
    details['contact'] = getDetail(elements[1], 'Contato')
    details['location'] = elements[0].find_elements_by_class_name('searchRightCol')[1].text
    details['company'] = elements[0].find_elements_by_class_name('searchRightCol')[0].text#getDetail(elements[0], 'Anunciante')
    details['type'] = getDetail(elements[1], 'Tipo de emprego')
    return details
    
def getDetail(masterElement, kw):
    ele1 = masterElement.find_elements_by_class_name('searchLeftCol')
    ele2 = masterElement.find_elements_by_class_name('searchRightCol')
    for i in range(len(ele1)):
        if ele1[i].text == kw:
            return ele2[i].text
    return 'Not Available'


def applyThroughCV(browser, us):
    BO.waitForElementLocated(browser, 'JOBG811', how='id')
    fn = browser.find_element_by_id('JOBG82')
    ln = browser.find_element_by_id('JOBG83')
    email = browser.find_element_by_id('JOBG811')
    fn.send_keys(us.personal['firstName'])
    ln.send_keys(us.personal['lastName'])
    email.send_keys(us.personal['email'])
    BO.waitForElementLocated(browser, 'chkPrefill', how='id')
    browser.execute_script("document.getElementById('chkPrefill').click();")
    element = browser.find_element_by_id('JOBG810019')
    element.find_element_by_xpath("//option[text()='Yes']").click()
    browser.find_element_by_id('JOBG837').send_keys(us.personal['CVPath'])
    time.sleep(3)
    browser.execute_script("document.getElementById('buttonApply').click();")
    time.sleep(2)
    #DONE
    
def applyToJob(browser, us, linkedIn=False):
    if linkedIn:
        #applyThroughLinkedIn(browser, us)
        pass
    else:
        applyThroughCV(browser, us)

def applyToAllUrls(browser, reflst, us):
    jobsearchurl = browser.current_url
    res = getJobSearchResults(browser)
    links = BO.getLinksFromElements(res)
    for link in links:
        browser.get(link)
        # we must verify that the page is the standard application page
        # neither is from indeed, or a vacancy completed or forbiden
        if BO.isElementPresent(browser,'searchContainer'):
            #if this element is present, we are in the correct page
            details = getJobDetails(browser)
            details['path'] = us.personal['LogPathJobsInGeneva']
            if str(details['reference']) not in reflst:
                applyToJob(browser, us)
                details['method'] = 'CV'
                DL.writeLogToCSV(details)
                reflst.add(details['reference'])
                time.sleep(2)
    browser.get(jobsearchurl)
    time.sleep(3)

def getBlockJobsAndApply():
    us = User('f')
    if os.path.isfile(us.personal['LogPathJobsInGeneva']):
        reflst = DL.getReferencesFromLog(us.personal['LogPathJobsInGeneva'])
    else:
        reflst = set()
    #here, unlike in pagepersonnel, the mainurl
    #contains already every job
    browser = BO.openNewBrowser(MAINURL)
    #we are now in page 1 of the results
    #for each page I wish to apply to every job
    applyToAllUrls(browser, reflst, us)
    while BO.isElementPresent(browser,'Next', 'link'):
        element = browser.find_element_by_link_text('Next')
        url = element.get_attribute('href')
        browser.get(url)
        applyToAllUrls(browser, reflst, us)
        time.sleep(2)
    time.sleep(5)
    #browser.close()

getBlockJobsAndApply()


print('done')
    
    