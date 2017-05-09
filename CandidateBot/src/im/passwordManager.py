# 
# @author David Moura <david.dbmoura at gmail.com>
# 


import re

path = 'C:/Users/David/Desktop/RandomPessoal/Pessoal/PW/pwFile.txt'

def getCredentialsFromFile(app):
    fp = open(path, 'r')
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
