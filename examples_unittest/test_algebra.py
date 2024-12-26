#! /usr/bin/env python

import unittest
# https://docs.python.org/3/library/unittest.html

import algebra  # Local module to be tested


class TestAlgebra(unittest.TestCase):

    def test_add(self):
        self.assertEqual(algebra.add(10, 5), 15)
        self.assertEqual(algebra.add(-10, 5), -5)  # Negative args
        self.assertEqual(algebra.add(10, -5), 5)
        self.assertEqual(algebra.add(0, 5), 5)  # Zero args
        self.assertEqual(algebra.add(5, 0), 5)
        self.assertEqual(algebra.add(5.1, 2), 7.1)  # Float args
        self.assertEqual(algebra.add(2.2, 5.5), 7.7)

    def test_subtract(self):
        self.assertEqual(algebra.subtract(10, 5), 5)
        self.assertEqual(algebra.subtract(-10, 5), -15)  # Negative args
        self.assertEqual(algebra.subtract(10, -5), 15)
        self.assertEqual(algebra.subtract(0, 5), -5)  # Zero args
        self.assertEqual(algebra.subtract(5, 0), 5)
        self.assertEqual(algebra.subtract(5, 1.5), 3.5)  # Float args w/neg
        self.assertEqual(algebra.subtract(-5.5, 2.25), -7.75)

    def test_multiply(self):
        self.assertEqual(algebra.multiply(10, 5), 50)
        self.assertEqual(algebra.multiply(-10, 5), -50)  # Negative args
        self.assertEqual(algebra.multiply(10, -5), -50)
        self.assertEqual(algebra.multiply(0, 5), 0)  # Zero args
        self.assertEqual(algebra.multiply(10, 0), 0)
        self.assertEqual(algebra.multiply(1.5, 5), 7.5)  # Float args w/neg
        self.assertEqual(algebra.multiply(-3, 1.5), -4.5)

    def test_divide(self):
        self.assertEqual(algebra.divide(10, 5), 2)
        self.assertEqual(algebra.divide(-10, 5), -2)  # Negative args
        self.assertEqual(algebra.divide(10, -5), -2)
        self.assertEqual(algebra.divide(0, 5), 0)  # Zero first arg

        # Divide by zero should raise ValueError
        # USAGE: assertRaises(exception, callable, *args, **kwargs)
        self.assertRaises(ValueError, algebra.divide, 10, 0)

        # Alternatively, using a context manager:
        with self.assertRaises(ValueError):
            algebra.divide(10, 0)

        self.assertEqual(algebra.divide(6, -2.5), -2.4)  # Float args w/neg
        self.assertEqual(algebra.divide(-4.5, 2), -2.25)


if __name__ == '__main__':
    unittest.main()

