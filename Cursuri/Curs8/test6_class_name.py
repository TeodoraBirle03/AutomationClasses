# cand vrem sa gasim mai multe elemente si le punem intr-o lista
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

# selector by Class - ia primul tot tp. - e ok doar daca avem clasa unica
chrome.find_element(By.CLASS_NAME, 'form-control').send_keys('Andy')

# gasim mai multe si punem in lista
chrome.find_elements(By.CLASS_NAME, 'form-control')[1].send_keys('Sinpetrean')


sleep(3)
chrome.quit()