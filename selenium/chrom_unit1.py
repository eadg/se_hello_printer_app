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
        self.driver = webdriver.Chrome()
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
        sleep(3)

    def testDrugi(self):
        # print("A teraz wykonuje prawdziwy test nr 2")
        pass

# Jesli program jest uruchomiony z tego pliku
if __name__=='__main__':
    # ... to uruchom testy
    unittest.main(verbosity=2)

