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
chrome.get('https://formy-project.herokuapp.com/')

# # selector by link_test
# chrome.find_element(By.LINK_TEXT, 'Enabled and disabled elements').click()
# sleep(2)
# chrome.find_element(By.CSS_SELECTOR, 'input[placeholder= "Input here..."]').send_keys('hartie')

# selector by partial_link_test
chrome.find_element(By.PARTIAL_LINK_TEXT, 'Drag').click()



sleep(3)
chrome.quit()