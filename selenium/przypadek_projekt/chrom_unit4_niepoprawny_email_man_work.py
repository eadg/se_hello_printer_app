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

    def testWrongEmail(self):
        driver = self.driver
        # 1. Kliknij "Zalguj sie"
        zaloguj_btn = WebDriverWait(driver, 60)\
        .until(EC.element_to_be_clickable((By.XPATH, '//button[@data-test="navigation-menu-signin"]')))
        zaloguj_btn.click()
        # 2. Kliknij "Rejestracja"
        rejestracja_btn = WebDriverWait(driver, 60)\
        .until(EC.element_to_be_clickable((By.XPATH, '//button[text()=" Rejestracja "]')))
        rejestracja_btn.click()
        # 3. Wprowadz imie
        name_field = WebDriverWait(driver, 60)\
        .until(EC.presence_of_element_located((By.NAME, 'firstName')))
        name_field.send_keys("Marek")
        # 4. Wprowadz nazwisko
        nazwisko_field=driver.find_element_by_name('lastName')
        nazwisko_field.send_keys("Nowak")
        # 5. Wybierz plec
        name_field.click()
        gender=driver.find_element_by_xpath('//label[@data-test="register-gendermale"]') # Mezczyzna
        gender.click()
        # 6. Wpisz kod kraju
        country_code=driver.find_element_by_xpath('//div[@data-test="booking-register-country-code"]')
        country_code.click()
        country_code_input=driver.find_element_by_name('phone-number-country-code')
        country_code_input.send_keys("+48")

        # 7. Wpisz numer telefonu
        phone=driver.find_element_by_name('phoneNumberValidDigits')
        phone.send_keys("123123123")
        # 8. Wpisz bledny e-mail
        email=driver.find_element_by_name('email')
        email.send_keys('sjahjhaf.pl')
        # 9. Wpisz haslo
        # 10. Wybierz kraj
        # 11. Zaakceptuj polityke prywatnosci
        # 12. Kliknij Zarejestruj sie


        # Czekam na koncu 5 sekund
        sleep(8)

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


