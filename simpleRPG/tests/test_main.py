import unittest
from games.cui.textbasedrpg.simpleRPG.main import simpleRPG


class TestMain(unittest.TestCase):
    def test_main(self):
        rpg = simpleRPG()
        self.assertTrue(rpg.main())


if __name__ == "__main__":
    unittest.main()