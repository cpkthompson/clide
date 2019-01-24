from util import find_sum
import unittest


class FindSumTest(unittest.TestCase):
    def test(self):
        self.assertEqual(find_sum(1, 2), 3)
