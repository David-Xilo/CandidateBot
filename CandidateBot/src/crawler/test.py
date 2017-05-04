# 
# @author David Moura <david.dbmoura at gmail.com>
# 

import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

#use to fill forms

chromepath = "C:/Users/David/Desktop/RandomPessoal/Software/chromedriver_win32/chromedriver.exe"
browser = webdriver.Chrome(chromepath)
browser.get('http://www.google.com')

browser.execute_script("window.open('http://google.com', 'new_window')")

browser.switch_to.window(browser.window_handles[0])

search = browser.find_element_by_name('q')
search.send_keys("google search through python")
search.send_keys(Keys.RETURN) # hit return after you enter search text

browser.switch_to.window(browser.window_handles[1])
search = browser.find_element_by_name('q')
search.send_keys("damn")
search.send_keys(Keys.RETURN) # hit return after you enter search text


time.sleep(1)
browser.quit()