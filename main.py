import os, sys
sys.path.append(os.path.dirname(sys.argv[0]))

import unittest


class TestSample(unittest.TestCase):

    def test_add_equal(self):
        a, b = 2, 5
        c = 7
        self.assertEqual(a+b, c)

    def test_add_true(self):
        a, b = 2, 5
        c = 7
        self.assertTrue(a+b==c)
        # in that case:
        # false
        # self.assertFalse()

    def test_add_instance(self):
        a,b = 2,5
        self.assertIsInstance(a+b, int)


if __name__ == "__main__":
    unittest.main()