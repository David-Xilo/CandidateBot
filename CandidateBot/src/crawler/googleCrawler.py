# 
# @author David Moura <david.dbmoura at gmail.com>
# 


import browserManagement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def seleniumGoogleSearch(browser, searchTerm):
    search = browser.find_element_by_name('q')
    search.send_keys(searchTerm)
    search.send_keys(Keys.RETURN)

def nextSearchPage(browser):
    try:
        click_icon = WebDriverWait(browser, 5, 0.25).until(EC.visibility_of_element_located([By.ID, 'pnnext']))
        click_icon.click()
        WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'main:not([style*="margin-top"])')))
    except:
        pass

def getLinksOfPageResults(browser):
    RESULTS_LOCATOR = "//div/h3/a"
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, RESULTS_LOCATOR)))
    page_results = browser.find_elements(By.XPATH, RESULTS_LOCATOR)
    links = []
    for item in page_results:
        links.append(item.get_attribute('href'))


#bm = browserManagement
#browser = bm.openNewBrowser()
#searchTerm = "software engineer junior geneva"
#seleniumGoogleSearch(browser, searchTerm)




