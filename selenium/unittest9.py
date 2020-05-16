"""
Scenariusz testowy:
Rejestracja na stronie www.automationpractice.com

Przypadek testowy
Bledny e-mail (Brak znaku '@')

Warunki wstepne:
Przegladarka otwarta na stronie www.automationpractice.com

Kroki:
1. Kliknij przycisk "Sign in"
2. Wpisz niepoprawny e-mail (brak znaku '@')
3. Kliknij "Create an account"

Oczekiwany rezultat:
1. Uzytkownik dostaje informacje
"Invalid email address."
(2. Konto nie zostaje zalozone)
"""


import unittest
from selenium import webdriver
from time import sleep

invalid_email="mareknowak.pl"

class TestRegistration(unittest.TestCase):
    """
    Scenariusz testowy:
    Rejestracja na stronie www.automationpractice.com
    """
    def setUp(self):
        """
        Warunki wstepne:
        Przegladarka otwarta na stronie www.automationpractice.com
        """
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("http://automationpractice.com/index.php")

    # Test sprawdzajacy - niepoprawny e-mail
    def testWrongEmail(self):
        """
        Przypadek testowy
        Bledny e-mail (Brak znaku '@')
        """
        driver = self.driver
        # 1. Kliknij przycisk "Sign in"
        sign_in_btn = driver.find_element_by_class_name('login')
        sign_in_btn.click()
        # 2. Wpisz niepoprawny e-mail (brak znaku '@')
        email_input = driver.find_element_by_id('email_create')
        email_input.send_keys(invalid_email)
        # 3. Kliknij "Create an account"
        driver.find_element_by_id('SubmitCreate').click()

        # Oczekiwany rezultat:
        # 1. Uzytkownik dostaje informacje
        # "Invalid email address."
        sleep(3)
        error = driver.find_element_by_xpath('//*[@id="create_account_error"]/ol/li')
        print(error.text)
        # Sprawdzam , czy uzytkownik otrzymal informacje "Invalid email address."
        assert "Invalid email address." == error.text
        # Poczekaj 3 sekundy
        sleep(3)

    def tearDown(self):
        """
        Zakonczenie testu
        """
        self.driver.quit()

if __name__=='__main__':
    unittest.main(verbosity=2)
