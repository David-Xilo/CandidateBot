# 
# @author David Moura <david.dbmoura at gmail.com>
# 

import browserManagement
import selenium
from im import passwordManager


appName = 'LinkedIn'
url = 'https://www.linkedin.com/uas/login'

def loginLinkedIn(browser):
    browserManagement.loadBrowserAndWaitForElement(browser, "session_key-login")
    credentials = passwordManager.getCredentialsFromFile('LinkedIn')
    elements = ("session_key-login", "session_password-login")
    browserManagement.login(browser, elements, credentials)


browser = browserManagement.openNewBrowser(url)
loginLinkedIn(browser)









