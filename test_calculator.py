"""Unit tests for the Calculator class."""

import unittest

from calculator import Calculator, CalculatorError


class CalculatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_basic_operations(self) -> None:
        self.assertEqual(self.calculator.add(8, 2), 10)
        self.assertEqual(self.calculator.subtract(8, 2), 6)
        self.assertEqual(self.calculator.multiply(8, 2), 16)
        self.assertEqual(self.calculator.divide(8, 2), 4)

    def test_power_and_modulus(self) -> None:
        self.assertEqual(self.calculator.power(3, 2), 9)
        self.assertEqual(self.calculator.modulus(10, 3), 1)

    def test_division_and_modulus_by_zero_raise_clear_errors(self) -> None:
        with self.assertRaises(CalculatorError):
            self.calculator.divide(10, 0)
        with self.assertRaises(CalculatorError):
            self.calculator.modulus(10, 0)

    def test_history_and_clear_history(self) -> None:
        self.calculator.add(1, 2)
        history = self.calculator.get_history()
        self.assertEqual(len(history), 1)
        self.assertEqual(history[0].result, 3)

        self.calculator.clear_history()
        self.assertEqual(self.calculator.get_history(), ())


if __name__ == "__main__":
    unittest.main()
