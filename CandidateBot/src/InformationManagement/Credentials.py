# 
# @author David Moura <david.dbmoura at gmail.com>
# 

import re

class User(object):
    def getLinkedInCredentials(self):
        print('Please Input your LinkedIn credentials')
        us = input('Username:')
        pw = input('Password:')
        self.username['LinkedIn'] = us
        self.password['LinkedIn'] = pw
    
    def setPersonalData(self):
        PWPath = 'C:/Users/David/Desktop/RandomPessoal/Pessoal/PW/PPI.txt'
        fp = open(PWPath, 'r')
        for line in fp:
            m = re.match('@([\S]*)', line)
            if m:
                what = m.group(1)
                line = next(fp)
                val = re.match('([\S]*)', line)
                self.personal[what] = val.group(1)
    
    def getCredentialsByFile(self):
        PWPath = 'C:/Users/David/Desktop/RandomPessoal/Pessoal/PW/pwFile.txt'
        fp = open(PWPath, 'r')
        for line in fp:
            m = re.match('@([\S]*)', line)
            if m:
                app = m.group(1)
                line = next(fp)
                u = re.match('User: ([\S]*)', line)
                line = next(fp)
                p = re.match('PW: ([\S]*)', line)
                self.username[app] = u.group(1)
                self.password[app] = p.group(1)
    
    def getAppCredentials(self, app):
        try:
            us = self.username[app]
            pw = self.password[app]
        except:
            print('no credentials for given app')
        return (us, pw)
    
    def __init__(self, char):
        self.username = {}
        self.password = {}
        self.personal = {}
        self.setPersonalData()
        if char == 'i':
            self.getLinkedInCredentials()
        if char == 'f':
            self.getCredentialsByFile()

#us = User('f')