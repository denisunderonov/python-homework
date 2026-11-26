import math
import unittest
from homework1.factorial import factorial
from homework1.median import find_median

class FactorialTests(unittest.TestCase):
    def test_negative(self):
        for n in (-100, -5, -1):
            with self.subTest(n=n):
                self.assertEqual(factorial(n), -1)

    def test_nonnegative(self):
        for n in (0, 1, 2, 5, 10, 12):
            with self.subTest(n=n):
                self.assertEqual(factorial(n), math.factorial(n))

class MedianTests(unittest.TestCase):
    def test_medians(self):
        cases = [('5 2 9 1 7', 5), ('4 1 8 5', 4.5), ('7', 7),
                 ('-10 -2 -4', -4), ('1 3', 2), ('-3 -2', -2.5),
                 ('2 2 8 8', 5), ('  3   1  2  ', 2), ('1000000 -1000000', 0)]
        for data, expected in cases:
            with self.subTest(data=data):
                result = find_median(data)
                self.assertEqual(result, expected)
                self.assertIs(type(result), int if isinstance(expected, int) else float)

if __name__ == '__main__':
    unittest.main()
