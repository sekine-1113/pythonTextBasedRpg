import unittest

from games.cui.textbasedrpg.simpleRPG.classes.player import MockPlayer


class TestPlayer(unittest.TestCase):
    def test_player(self):
        player = MockPlayer()
        self.assertEqual(player.name, "test")

    def test_get_parameters(self):
        player = MockPlayer()
        self.assertEqual(player.get_parameters(), None)


if __name__ == "__main__":
    unittest.main()
