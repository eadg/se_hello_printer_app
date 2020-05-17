import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

class WizzairRegistration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://wizzair.com/pl-pl#/")

    def testClickLogin(self):
        driver = self.driver
        # 1. Kliknij "Zalguj sie"
        zaloguj_btn = WebDriverWait(driver, 20)\
        .until(EC.element_to_be_clickable((By.XPATH, '//button[@data-test="navigation-menu-signin"]')))
        zaloguj_btn.click()

        # Czekam na koncu 3 sekundy
        sleep(3)

    def testInputWrong(self):
        '''extended by sing-in with mail '''
        invalid_email="mareknowak.pl"
        driver = self.driver
        # 1. Kliknij "Zalguj sie"
        zaloguj_btn = WebDriverWait(driver, 20)\
        .until(EC.element_to_be_clickable((By.XPATH, '//button[@data-test="navigation-menu-signin"]')))
        zaloguj_btn.click()
        # Czekam na koncu 3 sekundy
        sleep(3)
        input_mail = WebDriverWait(driver, 20)\
        .until(EC.element_to_be_clickable((By.XPATH, '//input[@data-test="login-modal-email"]')))
        input_mail.send_keys(invalid_email)
        driver.find_element_by_xpath('//button[@data-test="loginmodal-signin"]').click()
        sleep(3)


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
    
    
'''
Scenariusz testowy:
Rejestracja na stronie https://wizzair.com/pl-pl#/

Warunki wstepne:
Przegladarka otwarta na stronie https://wizzair.com/pl-pl#/

Przypadek testowy:
Bledny e-mail (Brak znaku '@')

Kroki:
1. Kliknij "Zalguj sie"
2. Kliknij "Rejestracja"
3. Wprowadz imie
4. Wprowadz nazwisko
5. Wybierz plec
6. Wpisz kod kraju
7. Wpisz numer telefonu
8. Wpisz bledny e-mail
9. Wpisz haslo
10. Wybierz kraj
11. Zaakceptuj polityke prywatnisci
12. Kliknij Zarejestruj sie

Oczekiwany rezultat:
1. Uzytkownik dostaje informacje "Nieprawidłowy adres e-mail"



FULL XPATH:
/html/body/div[2]/div/header/div[1]/div/nav/ul/li[11]/button

COPIED XPATH:
//*[@id="app"]/div/header/div[1]/div/nav/ul/li[11]/button

MY XPATH:
//button[@data-test="navigation-menu-signin"]

CSS SELECTOR:
button[data-test="navigation-menu-signin"]
'''


