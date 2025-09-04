import unittest

from Task0 import calculate


class TestCalculate(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculate(2, "+", 3), 5)
        self.assertAlmostEqual(calculate(2.5, "+", 0.1), 2.6, places=7)

    def test_subtraction(self):
        self.assertEqual(calculate(10, "-", 4), 6)
        self.assertAlmostEqual(calculate(2.5, "-", 0.1), 2.4, places=7)

    def test_multiplication(self):
        self.assertEqual(calculate(7, "*", 6), 42)
        self.assertAlmostEqual(calculate(2.5, "*", 0.2), 0.5, places=7)

    def test_division(self):
        self.assertEqual(calculate(8, "/", 2), 4)
        self.assertAlmostEqual(calculate(1, "/", 8), 0.125, places=7)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculate(1, "/", 0)

    def test_invalid_operator(self):
        with self.assertRaises(ValueError):
            calculate(2, "%", 3)


if __name__ == "__main__":
    unittest.main()


