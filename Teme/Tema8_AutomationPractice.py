# avem nevoie sa importam cateva librarii gratuite care ne ajuta sa controlam chrome
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# initializam chrome
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

# maximizam fereastra
chrome.maximize_window()

# navigam catre un url - oare de ce prima data apare in url data;; si apoi se redeschide
# iar chrome-ul cu url-ul specificat?
chrome.get('http://automationpractice.com/index.php')

# selector by ID
# search = chrome.find_element(By.ID, 'search_query_top')
# search.send_keys('Rochie lunga')
#
# # selector by class_name
# chrome.find_element(By.CLASS_NAME, 'bx-prev').click()
# sleep(1)

# # selector by ID
# email = chrome.find_element(By.ID, 'newsletter-input')
# email.send_keys('test@yahoo.com')
# sleep(2)

# selector by xpath
# chrome.find_element(By.XPATH, '//a[text() = "Women"]').click()
# sleep(1)
chrome.find_element(By.XPATH, '(//a[@title = "Printed Summer Dress"])[3]/parent::div/parent::div/parent::div//span[text() = "More"]').click()
sleep(1)
# chrome.find_element(By.XPATH, '//a[text() = "Contact us"]').click()
# sleep(1)
#
# # selector by ClassName
# chrome.find_element(By.CLASS_NAME, 'login').click()
#
# # selector by link_test
# chrome.find_element(By.LINK_TEXT, 'support@seleniumframework.com').click()
# sleep(1)

chrome.quit()

