# tests/test_cal.py
import unittest
from cal import somme, soustraction, produit, division

class TestCalculatrice(unittest.TestCase):
    def test_somme(self):
        self.assertEqual(somme(5, 3), 8)

    def test_soustraction(self):
        self.assertEqual(soustraction(5, 3), 2)

    def test_produit(self):
        self.assertEqual(produit(5, 3), 15)

    def test_division(self):
        self.assertEqual(division(6, 3), 2)
        with self.assertRaises(ZeroDivisionError):
            division(6, 0)

if __name__ == "__main__":
    unittest.main()
