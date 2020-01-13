import unittest
from FizzBuzz import FB


class testFB(unittest.TestCase):
    def test_1(self):
        self.assertEqual(1, FB(1))

    def test_3(self):
        self.assertEqual("Fizz", FB(3))

    def test_5(self):
        self.assertEqual("Buzz", FB(5))

    def test_15(self):
        self.assertEqual("FizzBuzz", FB(15))


if __name__ == "__main__":
    unittest.main()
