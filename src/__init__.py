#! python3
# Facebook Post - Logs in and post something on facebook automatically

import time
import os
from selenium import webdriver

email = 'your_email'
password = 'your_password'
post = 'your_post'

chrome_driver = './chromedriver.exe'
os.environ['webdriver.chrome.driver'] = chrome_driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('prefs', {"profile.default_content_setting_values.notifications": 2})
browser = webdriver.Chrome(executable_path=chrome_driver, chrome_options=chrome_options)
browser.get('https://www.facebook.com/')

# login
browser.find_element_by_id('email').send_keys(email)
password_field = browser.find_element_by_id('pass')
password_field.send_keys(password)
password_field.submit()
# post something
browser.find_element_by_class_name('_559p').click()

status = browser.switch_to.active_element
status.send_keys(post)
browser.find_element_by_css_selector('button._4jy0._4jy3._4jy1').click()
browser.find_element_by_css_selector('button._1mf7._4jy0._4jy3').click()

time.sleep(5)
browser.quit()
