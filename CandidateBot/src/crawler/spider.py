# 
# @author David Moura <david.dbmoura at gmail.com>
# 

import google
from selenium import webdriver


def googleSearch(search_term, clicks):
    urllist = []
    for url in google.search(search_term , stop = clicks):
        urllist.append(url)
    return urllist

urllist = googleSearch("software engineering jobs junior geneva", 10)

chromepath = "C:/Users/David/Desktop/RandomPessoal/Software/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(chromepath)

driver.get(urllist[0])

#for url in google.search("david", stop = 2):
#    print(url)
#    driver.get(url)
#search_box = driver.find_element_by_name('q')
#search_box.send_keys('ChromeDriver')
#search_box.submit()


