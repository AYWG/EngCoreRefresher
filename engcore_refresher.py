# A script that logs into UBC EngCore and refreshes the page every 9 minutes
# and 29 seconds. This prevents the the user from being automatically logged out
# due to inactivity.

import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
                   
# open chrome                   
driver = webdriver.Chrome(os.getenv('chromedriver')) # replace os.getenv('chromedriver') with path to chromedriver.exe

# go to the login url
driver.get(os.getenv('url_refresh')) # replace os.getenv('url_refresh') with link to login url

# retrieve the necessary webpage elements for logging in
username = driver.find_element_by_id('j_username')
password = driver.find_element_by_id('password')
form = driver.find_element_by_name('loginForm')

# fill in user / password and submit
username.send_keys(os.getenv('cwl_user')) # replace os.getenv('cwl_user') with CWL username
password.send_keys(os.getenv('cwl_password')) # replace os.getenv('cwl_password') with CWL password
form.submit()

while 1:
	# refresh every 9 minutes and 25 seconds
    time.sleep(565)
    driver.refresh()

