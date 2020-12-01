#! /usr/bin/env python

"""
-----------------------------------------------------------------------
 Description:  Run simple addition test for simple_calculator.py

 Assumptions:

 Command line arguments: none

 Usage: python test_simple_calculator.py       # run the unit tests
-----------------------------------------------------------------------
"""

import unittest
import sys
import os

_TEST_DIR = os.path.dirname(os.path.abspath(__file__))
_SCRIPTS_DIR = os.path.abspath(os.path.join(_TEST_DIR, os.pardir, "scripts"))

if not os.path.exists(_SCRIPTS_DIR):
    raise ImportError("Cannot find scripts directory")

sys.path.append(_SCRIPTS_DIR)

# pylint: disable=wrong-import-position
from simple_calculator import SimpleCalculator
# pylint: enable=wrong-import-position

class AdditionTestSuite(unittest.TestCase):
    """Unit test for simple_calculator"""
    def setUp(self):
        """ Executed before every test case to create SimpleCalculator object """
        self.calculator = SimpleCalculator()

    def test_addition_two_integers(self):
        """ Test that adding two positive numbers returns the correct sum """
        result = self.calculator.sum(5, 6)
        self.assertEqual(result, 11)

    def test_addition_integer_string(self):
        """ Test that adding an integer and a string returns an error """
        result = self.calculator.sum(5, "6")
        self.assertEqual(result, "ERROR")

    def test_addition_negative_integers(self):
        """ Test that adding two negative numbers returns the correct sum """
        result = self.calculator.sum(-5, -6)
        self.assertEqual(result, -11)
        self.assertNotEqual(result, 11)

    def test_multiply_two_integers(self):
        """ Test that multiplying two positive numbers returns the correct number """
        result = self.calculator.multiply(5, 6)
        self.assertEqual(result, 30)

    def test_multiply_negative_integers(self):
        """ Test that multiplying two negative numbers returns the correct number """
        result = self.calculator.multiply(-5, -6)
        self.assertEqual(result, 30)

    def test_multiply_integer_string(self):
        """ Test that multiplying a negative number and a string returns an error """
        result = self.calculator.multiply(-5, "-6")
        self.assertEqual(result, "ERROR")

# Execute all the tests when the file is executed
if __name__ == "__main__":
    unittest.main()
