# 
# @author David Moura <david.dbmoura at gmail.com>
# 

import browserManagement as BM
#import selenium
#from im import passwordManager
from im.credentialManager import Me
import re
#appName = 'LinkedIn'
#url = 'https://www.linkedin.com/uas/login'

PWPath = 'C:/Users/David/Desktop/RandomPessoal/Pessoal/PW/pwFile.txt'

def getCredentialsFromFile(app):
        fp = open(PWPath, 'r')
        user = None
        pw = None
        for line in fp:
            if app in line:
                for line in fp:
                    m = re.match('User: ([\S]*)', line)
                    p = re.match('PW: ([\S]*)', line)
                    if m:
                        user = m.group(1)
                    if p:
                        pw = p.group(1)
        return (user, pw)

#TODO
def loginLinkedIn(browser):
    BM.waitForElementLocated(browser, 'id', "session_key-oauth2SAuthorizeForm")
    credentials = getCredentialsFromFile('LinkedIn')
    elements = ("session_key-oauth2SAuthorizeForm", "session_password-oauth2SAuthorizeForm")
    BM.login(browser, elements, credentials)









