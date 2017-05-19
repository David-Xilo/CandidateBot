# 
# @author David Moura <david.dbmoura at gmail.com>
# 


import Spider.BrowserOps as BO
from InformationManagement.Credentials import User
from selenium.webdriver.common.keys import Keys
import time
import InformationManagement.DataLog as DL
import os
import re

MAINURL = 'https://www.experis.ch/jobs/?sortdir=desc&pagesize=96&sortby=WebsiteDate'

def loginToSite(browser, us):
    BO.waitForElementLocated(browser, 'CPHMain_CPHContent_CandidateLogin1_Login1_UserName', how='id')
    email = browser.find_element_by_id('CPHMain_CPHContent_CandidateLogin1_Login1_UserName')
    email.send_keys(us.username['GMail'])
    pw = browser.find_element_by_id('CPHMain_CPHContent_CandidateLogin1_Login1_Password')
    pw.send_keys(us.password['GMail'])
    browser.execute_script("document.getElementById('CPHMain_CPHContent_CandidateLogin1_Login1_LoginButton').click();")

def getJobSearchResults(browser):
    BO.waitForElementLocated(browser, 'apply', how='class')
    page_results = browser.find_elements_by_class_name('apply')
    results = []
    for item in page_results:
        results.append(item)
    return results

    
def getJobDetails(browser): 
    details = {}
    loc = getDetail(browser, "location")[0].text
    ref = getDetail(browser, "reference")[0].text
    tp = getDetail(browser, "job-type")[0].text
    m = re.match('[\S\s]*?:\s([\S\s]*)', loc)
    loc = m.group(1)
    m = re.match('[\S\s]*?:\s([\S\s]*)', ref)
    ref = m.group(1)
    m = re.match('[\S\s]*?:\s([\S\s]*)', tp)
    tp = m.group(1)
    details['jobName'] = getDetail(browser, "job-title")[0].text
    details['reference'] = ref
    details['contact'] = getDetail(browser, "profileWidgetTitle")[0].text
    details['location'] = loc
    details['company'] = 'Experis'#getDetail(browser, "field-name-field-job-desc-company")
    details['type'] = tp
    return details
    
def getDetail(browser, identifier):
    BO.waitForElementLocated(browser, identifier, how='class')
    ele = browser.find_elements_by_class_name(identifier)
    return ele

def applyThroughWebSite(browser, us):
    if BO.isElementPresent(browser, 'CPHMain_CPHContent_CandidateLogin1_Login1_UserName', how='id'):
        loginToSite(browser, us)
    BO.waitForElementLocated(browser, 'ctl00_CPHMain_CPHContent_AsyncFileUploader_RadAsyncUpload1file0', how='id')
    browser.find_element_by_id('ctl00_CPHMain_CPHContent_AsyncFileUploader_RadAsyncUpload1file0').send_keys(us.personal['CVPath'])
    browser.execute_script("document.getElementById('CPHMain_CPHContent_rdoCandidateFiles_4').click();")
    with open(us.personal['CoverText1'], 'r') as myfile:
        data = myfile.read()
    browser.find_element_by_id('CPHMain_CPHContent_txtCoverNote').send_keys(data)
    time.sleep(2)
    browser.execute_script("document.getElementById('CPHMain_CPHContent_btnSubmit').click();")

def applyThroughCV(browser, us):
    pass
    
def applyToJob(browser, us, website=True):
    #this website has image recognition challenges, unless we are signed in (through GMail)
    browser.execute_script("document.getElementById('CPHMain_CPHContent_hylLoginToApply2').click();")
    if website:
        applyThroughWebSite(browser, us)
    else:
        applyThroughCV(browser, us)

def applyToAllUrls(browser, reflst, us):
    jobsearchurl = browser.current_url
    res = getJobSearchResults(browser)
    links = BO.getLinksFromElements(res)
    for link in links:
        browser.get(link)
        details = getJobDetails(browser)
        details['path'] = us.personal['LogPathExperis']
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
    if os.path.isfile(us.personal['LogPathExperis']):
        reflst = DL.getReferencesFromLog(us.personal['LogPathExperis'])
    else:
        reflst = set()
    browser = BO.openNewBrowser(MAINURL)
    #we are now in page 1 of the results
    #for each page I wish to apply to every job
    applyToAllUrls(browser, reflst, us)
    BO.waitForElementLocated(browser, 'pagingHeader_lnkNextPageItem', how='id', delay = 30)
    #BUG : TODO
    while BO.isElementPresent(browser,'pagingHeader_lnkNextPageItem', how='id'):
        browser.execute_script("document.getElementById('pagingHeader_lnkNextPageItem').click();")
        applyToAllUrls(browser, reflst, us)
        time.sleep(2)
    time.sleep(10)
    #browser.close()

getBlockJobsAndApply()


print('done')
    
    