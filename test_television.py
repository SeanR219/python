import unittest
from television import *


class MyTestCase(unittest.TestCase):

    def test_init(self):
        tv = Television()
        self.assertEqual(str(tv), 'Power = False, Channel = 0, Volume = 0')


if __name__ == '__main__':
    unittest.main()
