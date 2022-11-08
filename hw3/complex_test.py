from complex import Complex
import unittest

class TestComplex(unittest.TestCase):

    def test_add1(self):
        first = Complex(2, 5)
        second = Complex(3, 2)
        expected = Complex(5, 7)
        self.assertEqual(first + second, expected)

    def test_add2(self):
        import random

        for i in range(1000):
            re1, re2, im1, im2 = random.random(), random.random(), random.random(), random.random()
            python_complex1 = complex(re1, im1)
            python_complex2 = complex(re2, im2)

            my_complex1 = Complex(re1, im1)
            my_complex2 = Complex(re2, im2)

            expected = Complex(python_complex1.real + python_complex2.real,
                                 python_complex1.imag + python_complex2.imag)

            self.assertEqual(my_complex1 + my_complex2, expected)

    def test_subtract1(self):
        first = Complex(2, 5)
        second = Complex(3, 2)
        expected = Complex(-1, 3)
        self.assertEqual(first - second, expected)

    def test_multiply1(self):
        first = Complex(2, 5)
        second = Complex(3, 2)
        expected = Complex(-4, 19)
        self.assertEqual(first * second, expected)

    def test_divide1(self):
        first = Complex(1, 2)
        second = Complex(3, 4)
        expected = Complex(0.44, 0.08)
        self.assertEqual(first / second, expected)

    def test_dicide2(self):
        first = Complex(1, 2)
        second = Complex(0, 0)
        self.assertEqual(first / second, None)

if __name__ == "__main__":
    unittest.main()


