# arquivo: test_roman_converter.py
import unittest
from conversor_int_romanos import int_to_roman

class TestRomanConverter(unittest.TestCase):
    def test_single_digits(self):
        self.assertEqual(int_to_roman(1), "I")
        self.assertEqual(int_to_roman(4), "IV")
        self.assertEqual(int_to_roman(9), "IX")
        self.assertEqual(int_to_roman(5), "V")
        self.assertEqual(int_to_roman(10), "X")

    def test_double_digits(self):
        self.assertEqual(int_to_roman(40), "XL")
        self.assertEqual(int_to_roman(90), "XC")
        self.assertEqual(int_to_roman(50), "L")
        self.assertEqual(int_to_roman(60), "LX")
        self.assertEqual(int_to_roman(99), "XCIX")

    def test_triple_digits(self):
        self.assertEqual(int_to_roman(400), "CD")
        self.assertEqual(int_to_roman(900), "CM")
        self.assertEqual(int_to_roman(500), "D")
        self.assertEqual(int_to_roman(1000), "M")
        self.assertEqual(int_to_roman(3999), "MMMCMXCIX")

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            int_to_roman(0)
        with self.assertRaises(ValueError):
            int_to_roman(-1)
        with self.assertRaises(ValueError):
            int_to_roman(4000)

if __name__ == "__main__":
    unittest.main()
