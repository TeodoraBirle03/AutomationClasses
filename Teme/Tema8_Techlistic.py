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
chrome.find_element(By.XPATH, '//button[@id="ez-accept-all"]').click()
sleep(2)

# completam inputul pt first_name si last_name
first_name = chrome.find_element(By.XPATH, '//input[@name="firstname"]')
first_name.send_keys('Popescu')
last_name = chrome.find_element(By.XPATH, '//input[@name="lastname"]')
last_name.send_keys('Alexandra')

# alegem Female si 3 ani Experienta
chrome.find_element(By.XPATH, '//input[@id="sex-1"]').click()
sleep(2)
chrome.find_element(By.XPATH, '//input[@id="exp-2"]').click()

sleep(2)
chrome.quit()
