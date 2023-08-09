'''Write a simple caluculater class such that:
add method
multiply
divide'''
import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()
    def test_add_two_positive_numbers_together(self):
        self.assertEqual(self.calculator.add(3,4), 7)
        #arrange #act # assert

    def test_add_two_strings_together(self):
        #calculator = Calculator()
        self.assertEqual(self.calculator.add("ap","ple"), "apple")

    def test_add_number_to_string_raises_type_error(self):
        #calculator = Calculator()
        self.assertRaises(self.calculator.add(3,"apple"))

    def test_multiply_two_positive_numbers_together(self):
        self.assertEqual(self.calculator.multiply(3,4), 12)

    def test_multiply_two_use_floart_together(self):
        self.assertRaises(self.calculator.multiply("apple","orange"))

    def test_divide_two_positive_numbers_together(self):
        self.assertEqual(self.calculator.divide(6,3), 2)

