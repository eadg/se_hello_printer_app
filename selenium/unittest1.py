import unittest

class First(unittest.TestCase):
    
    def setUp(self):
        print('przygotowanie')

    def tearDown(self):
        print('czyszczenie')

    def test1(self):
        print('test1')

    def test2(self):
        print('test2')

if __name__ == '__main__':
    unittest.main()
