# Import niezbednych bibliotek
import unittest
from selenium import webdriver
from time import sleep # sleep(3)
# import time # time.sleep(3)

# Przygotowuje szkielet testow w unittescie
class MojPierwszyPrzypadekTestowy(unittest.TestCase):
    # Przed kazdym testem
    def setUp(self):
        #print("Przygotowuje test")
        # Wlaczam Fireofoxa
        self.driver = webdriver.Firefox()
        # Otworz strone google
        self.driver.get("http://www.google.pl")
        # Makzymalizacja okna
        self.driver.maximize_window()

    # Sprzatanie po kazdym tescie
    def tearDown(self):
        # print("Sprzatam po tescie")
        # Wylaczam przegladarke
        self.driver.quit()

    def testPierwszy(self):
        #print("A teraz wykonuje prawdziwy test nr 1")
        #assert 2==3
        driver = self.driver
        # Szukam pola wyszukiwania
        search_field = driver.find_element_by_name('q')
        # Wpisuje w pole wyszukiwania "tester"
        search_field.send_keys("tester")
        # Wysylam formularz (tak jakbym wcisnal ENTER)
        search_field.submit()
        # Czekam 3 sekundy
        sleep(3)
        # Przechwytuje wyniki wyszukiwania
        results =driver.find_elements_by_class_name('g')
        # Sprawdzam ile znalazlem WebElementow o klasie g
        # (wynikow wyszukiwania)
        print(len(results))
        sleep(3)

# Jesli program jest uruchomiony z tego pliku
if __name__=='__main__':
    # ... to uruchom testy
    unittest.main(verbosity=2)

