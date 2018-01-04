import unittest
from unnecessary_math import multiply
from unnecessary_math import add
from unnecessary_math import subtract
from unnecessary_math import divide
from str_func import *


class HelloWorld(unittest.TestCase):

    def setUp(self):
        pass

    def test_numbers_3_4(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_strings_a_3(self):
        self.assertEqual(multiply('a', 3), 'aaa')

    def test_numbers_4_3_fail(self):
        self.assertEqual(add(4, 3), 7)

    def test_numbers_4_3(self):
        self.assertEqual(subtract(4, 3), 1)

    def test_numbers_20_5(self):
        self.assertEqual(divide(20, 5), 4)

    def test_str_func1(self):
        self.assertEqual(reverse('abc'), 'cba')


if __name__ == '__main__':
    print("Hello World")
    print("Hello Galaxy")
    print("Hello Universe")
    unittest.main()



