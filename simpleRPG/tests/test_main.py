import unittest
from games.cui.textbasedrpg.simpleRPG import main


class TestMain(unittest.TestCase):
    def test_main(self):
        self.assertTrue(main.main())


if __name__ == "__main__":
    unittest.main()