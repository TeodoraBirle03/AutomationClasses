import unittest
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Login(unittest.TestCase):
    # punem elementele din pagina:
    LOGIN_LABEL = (By.XPATH, '//h2')
    USERNAME_INPUT = (By.XPATH, '//input[@id="username"]')
    PASS_INPUT = (By.XPATH, '//input[@id="password"]')
    LOGIN_BUTTON = (By.XPATH, '//button/i')
    ELEMENTAL_LINK = (By.XPATH, '//a[@href = "http://elementalselenium.com/"]')
    ERROR_LOGIN = (By.XPATH, '//div[@class="flash error"]')
    X_BUTTON = (By.XPATH, '//a[@class="close"]')
    USERNAME_INPUT = (By.XPATH, '(//label)[1]')
    PASSWORD_INPUT = (By.XPATH, '(//label)[2]')

    def test9_label_test(self):
        lista_label = self.chrome.find_elements(By.XPATH, '//label')
        actual = (self.chrome.find_elements(By.XPATH, '//label'))[1].text
        expected = 'Username'
        self.assertEqual(actual, expected, "Username label text it's inccorect")

