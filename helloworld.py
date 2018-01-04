import unittest
from unnecessary_math import multiply
from unnecessary_math import add


class HelloWorld(unittest.TestCase):

    def setUp(self):
        pass

    def test_numbers_3_4(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_strings_a_3(self):
        self.assertEqual(multiply('a', 3), 'aaa')

    def test_numbers_4_3(self):
        self.assertEqual(add(4,3),7)


if __name__ == '__main__':
    print("Hello World")
    print("Hello Galaxy")
    print("Hello Universe")
    unittest.main()



