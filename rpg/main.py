import unittest


class TestTashizan(unittest.TestCase):
    """test class of tashizan
    """

    def test_tashizan(self):
        """test method for tashizan
        """
        val1 = 1
        val2 = 5
        ans = 6
        self.assertEqual(ans, val1+val2)


if __name__ == "__main__":
    unittest.main()