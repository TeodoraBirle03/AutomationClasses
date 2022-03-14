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

# navigam catre un url
chrome.get('https://formy-project.herokuapp.com/form')

# selector by ID
first_name = chrome.find_element(By.ID, 'first-name')
first_name.send_keys('Teodora')

last_name = chrome.find_element(By.ID, 'last-name')
last_name.send_keys('Birle')
sleep(3)
chrome.quit()