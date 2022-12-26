import unittest

from games.cui.textbasedrpg.alpha.main import main


class TestMain(unittest.TestCase):

    def test_main(self):
        self.assertEqual(main(), 0)


if __name__ == "__main__":
    unittest.main()
