import unittest
from FizzBuzz import FB

x = [1, 3, 5, 15]
y = [1, "Fizz", "Buzz", "FizzBuzz"]


class testFB(unittest.TestCase):
    def test_case(self):
        for i in zip(x, y):
            self.assertEqual(i[1], FB(i[0]))


if __name__ == "__main__":
    unittest.main()
