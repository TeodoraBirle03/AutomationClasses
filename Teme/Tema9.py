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


    # se rulaza inainte de fiecare test
    def setUp(self):
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get('https://the-internet.herokuapp.com/')
        self.chrome.implicitly_wait(5)
        self.chrome.find_element(By.XPATH, '(//a[text() = "Form Authentication"])').click()

    # se ruleaza dupa fiecare test
    def tearDown(self):
        self.chrome.quit()

    # se verifica ca noul url e corect
    def test1_url(self):
        actual = self.chrome.current_url
        expected = ('https://the-internet.herokuapp.com/login')
        # expected value, actual value, mesaj in caz de fail
        self.assertEqual(expected, actual, 'URL is incorrect')
        # WebDriverWait(self.chrome, 2).until(EC.url_changes('https://the-internet.herokuapp.com/login'))

    # verificam page title
    def test2_page_title(self):
        actual = self.chrome.title
        expected = 'The Internet'
        self.assertEqual(expected, actual, 'Page title is incorrect')

    # Verificati textul de pe elementul xpath=//h2 e corect
    def test3_label(self):
        actual = self.chrome.find_element(*self.LOGIN_LABEL).text
        expected = 'Login Page'
        self.assertEqual(expected, actual, 'The text label is inccorect')

    # Verificati ca butonul de login este displayed
    def test4_buton_login(self):
        login = self.chrome.find_element(*self.LOGIN_BUTTON)
        self.assertTrue(login.is_displayed(), 'Login button is not displayed')

    # Verificati ca atributul href al linkului 'Elemental Selenium' e corect
    def test5_atribut_link(self):
        actual = self.chrome.find_element(*self.ELEMENTAL_LINK).get_attribute('href')
        expected = 'http://elementalselenium.com/'
        self.assertEqual(actual, expected, "Link Elemental Selenium doesn't have href atribute")

    '''Test6 Lasati goale user si pass
        Click login
        Verifica ca eroarea e displayed'''

    def test6_error_displayed(self):
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        error = self.chrome.find_element(*self.ERROR_LOGIN)
        self.assertTrue(error.is_displayed(), f"The {error} it's not displayed")

    '''Test7
    Completeaza cu user si pass invalide
    Click login
    Verifica ca mesajul de pe eroare e corect
    Este si un x pus acolo extra asa ca vom folosi solutia de mai jos
    expected = 'Your username is invalid!'
    self.assertTrue(expected in actual, 'Error message text is incorrect')
'''

    def test7_error_displayed(self):
        self.chrome.find_element(*self.USERNAME_INPUT).send_keys('Name')
        self.chrome.find_element(*self.PASS_INPUT).send_keys('Pass')
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        actual = self.chrome.find_element(*self.ERROR_LOGIN).text
        print(actual)
        expected = 'Your username is invalid!'
        self.assertTrue(expected in actual, 'Error message text is incorrect')

    '''Test8
    Lasati goale user si pass
    Click login
    Apasa x la eroare
    Verifica ca eroarea a disparut'''

    def test8_error_not_displayed(self):
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        sleep(2)
        self.chrome.find_element(*self.X_BUTTON).click()
        sleep(1)
        try:
            self.chrome.find_element(*self.ERROR_LOGIN)
            raise Exception("The error message is still displayed!")
        except NoSuchElementException:
            pass

    '''Test9
    Ia ca o lista toate //label
    Verifica textul ca textul de pe ele sa fie cel asteptat (Username si Password)
    Aici e ok sa avem 2 asserturi
    '''

    def test9_label_test(self):
        lista_label = self.chrome.find_elements(By.XPATH, '//label')
        actual = (lista_label)[0].text
        expected = 'Username'
        self.assertEqual(actual, expected, "Username label text it's inccorect")
        actual2 = (lista_label)[1].text
        expected2 = 'Password'
        self.assertEqual(actual2, expected2, "Password label text it's inccorect")

        '''Test10
    Completeaza cu user si pass valide
    Click login
    Verifica ca noul url CONTINE /secure
    Foloseste un explicit wait pentru elementul cu clasa ’flash succes’
    Verifica ca elementul cu clasa=’flash succes’ este displayed
    Verifica ca mesajul de pe acest element CONTINE textul ‘secure area!’'''

    def test10_login_flow(self):
        # Completeaza cu user si pass valide
        self.chrome.find_element(*self.USERNAME_INPUT).send_keys('tomsmith')
        self.chrome.find_element(*self.PASS_INPUT).send_keys('SuperSecretPassword!')
        # Click login
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        # Verifica ca noul url CONTINE /secure
        actual = self.chrome.current_url
        expected = 'secure'
        self.assertTrue(expected in actual, "The link doesn't contains secure")
        # Foloseste un explicit wait pentru elementul cu clasa ’flash succes’
        try:
            WebDriverWait(self.chrome, 5).\
                until(EC.presence_of_element_located((By.XPATH, '//div/div[@class="flash success"]')))
        except TimeoutException:
            self.assertTrue\
                (False, "I've been waiting for 5 seconds but I haven't found the element with 'flash success' class")
        # Verifica ca elementul cu clasa=’flash succes’ este displayed
        elem = self.chrome.find_element(By.XPATH, '//div/div[@class="flash success"]')
        self.assertTrue(elem.is_displayed(), 'Not the green element')
        # Verifica ca mesajul de pe acest element CONTINE textul ‘secure area!
        actual2 = elem.text
        expected2 = 'secure area'
        self.assertTrue(expected2 in actual2, 'The text of the green elem does NOT contain secure area')

    '''Test11
    Completeaza cu user si pass valide
    Click login
    Click logout
    Verifica ca ai ajuns pe https://the-internet.herokuapp.com/login
    '''
    def test11_login_logout(self):
        # Completeaza cu user si pass valide
        self.chrome.find_element(*self.USERNAME_INPUT).send_keys('tomsmith')
        self.chrome.find_element(*self.PASS_INPUT).send_keys('SuperSecretPassword!')
        # Click login
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        sleep(2)
        # Click logout
        self.chrome.find_element(By.XPATH, '//i[@class="icon-2x icon-signout"]').click()
        # Verifica ca ai ajuns pe https://the-internet.herokuapp.com/login
        actual = self.chrome.current_url
        expected = 'https://the-internet.herokuapp.com/login'
        self.assertEqual(actual, expected, "You are NOT in the right place")

        '''BONUS Test12 - brute force password hacking
    Completeaza user tomsmith
    Gaseste elementul //h4 
    Ia textu de pe el si fa split dupa spatiu. Considera fiecare cuvant ca o potentiala parola
    Foloseste o structura iterativa prin care sa introduci rand pe rand parolele si sa apesi pe login
    La final testul trebuie sa imi printeze fie
	‘Nu am reusit sa gasesc parola’
	‘Parola secreta este [parola]’ '''

    # def test12_secret_password(self):
    #     # Completeaza cu user valid
    #     self.chrome.find_element(*self.USERNAME_INPUT).send_keys('tomsmith')
    #     text_paragraph = self.chrome.find_element(By.XPATH, '//h4[@class="subheader"]').text
    #     print(text_paragraph)
    #     word_list = text_paragraph.split(' ')
    #     print(word_list)
    #     i = 0
    #     while i <= len(word_list):
    #         password = word_list[i]
    #         i = i+1
    #         self.chrome.find_element(*self.PASS_INPUT).send_keys(password)
    #         if password == "SuperSecretPassword!":
    #             print (f'Parola secreta este {password}')
    #             continue
    #         else:
    #             print(f'Nu am reusit sa gasesc parola')
