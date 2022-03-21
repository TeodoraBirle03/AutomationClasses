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

# accesam site-ul
chrome.get('https://www.techlistic.com/p/selenium-practice-form.html')

# dam click pe butonul de pe pop-up-up de cookies (Continue...)
chrome.find_element(By.XPATH, '//*[@id="ez-accept-all"]').click()
sleep(2)

# completam inputul pt first_name
first_name = chrome.find_element(By.XPATH, '//*[@id="post-body-3077692503353518311"]/div[1]/div/div/h2[2]/div[1]/div/div[2]/input')
first_name.send_keys('Popescu')

# chrome.find_element(By.XPATH, '//*[@id="cookieChoiceDismiss"]').click()
# sleep(2)

last_name = chrome.find_element(By.XPATH, '//*[@id="post-body-3077692503353518311"]/div[1]/div/div/h2[2]/div[1]/div/div[5]/input')
last_name.send_keys('Alexandra')

chrome.find_element(By.ID, 'sex-1').click()
chrome.find_element(By.ID, 'exp-1').click()

sleep(3)
chrome.quit()
