import unittest
from time import sleep
from datetime import date
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Flights_search(unittest.TestCase):
    # punem elementele din pagina
    FLIGHTS_BTN = (By.XPATH, '(//button[@id= "hotels-tab" ])[2]')
    ONE_WAY_RADIO = (By.XPATH, '//input[@id="one-way"]')
    ROUND_WAY_RADIO = (By.XPATH, '//input[@id="round-trip"]')
    FLYING_FROM_INPUT = (By.XPATH, '// input[@id = "autocomplete"]')
    DESTINATION_INPUT = (By.XPATH, '//input[@id="autocomplete2"]')
    FLIGHT_TYPE_DROPDWN = (By.XPATH, '//select[@id="flight_type"]/option[@value="economy_premium"]')
    DEPARTURE_DATE_INPUT = (By.XPATH, '(//input[@id="departure"])[1]')
    PASSENGERS_DROPDWN = (By.XPATH, '(//a[@href="#"])[2]')
    SEARCH_BTN = (By.XPATH, '//button[@id="flights-search"]')


    # se rulaza inainte de fiecare test
    def setUp(self):
        s = Service(GeckoDriverManager().install())
        self.driver = webdriver.Firefox(service=s)
        self.driver.maximize_window()
        self.driver.get('https://www.phptravels.net/')
        self.driver.implicitly_wait(5)

    # se ruleaza dupa fiecare test
    def tearDown(self):
        self.driver.quit()

    # verificam page title
    def test1_page_title(self):
        actual = self.driver.title
        expected = 'PHPTRAVELS - PHPTRAVELS'
        self.assertEqual(expected, actual, 'Page title is incorrect')

    # click pe tab-ul/button-ul de Flights
    def test2_flights(self):
        self.driver.find_element(*self.FLIGHTS_BTN).click()
        sleep(1)
        self.driver.find_element(*self.ONE_WAY_RADIO).click()
        self.driver.find_element(*self.FLYING_FROM_INPUT).send_keys('Cluj')
        self.driver.find_element(By.XPATH, '//div[contains(text(), "Cluj-napoca")]').click()
        self.driver.find_element(*self.FLIGHT_TYPE_DROPDWN).click()
        self.driver.find_element(*self.DESTINATION_INPUT).send_keys('Rome')
        self.driver.find_element(By.XPATH, '//div[@data-index="1"]').click()
        self.driver.find_element(*self.DEPARTURE_DATE_INPUT).click()
        self.driver.find_element(By.XPATH, '(//div[@class="datepicker-days"])[3]//td[text()="20"]').click()
        self.driver.find_element(*self.PASSENGERS_DROPDWN).click()
        self.driver.find_element(By.XPATH, '//input[@id="fadults"]/following-sibling::div/i').click()
        self.driver.find_element(By.XPATH, '//input[@id="fchilds"]/following-sibling::div/i').click()
        sleep(1)
        self.driver.find_element(*self.SEARCH_BTN).click()
        sleep(2)
        actual = self.driver.current_url
        expected = ('https://www.phptravels.net/flights/en/usd/clj/fco/oneway/economy_premium/20-04-2022/2/1/0')
        self.assertEqual(expected, actual, 'You have landed on a wrong page/url')