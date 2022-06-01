import unittest

from games.cui.textbasedrpg.simpleRPG.classes.player import Player


class TestPlayer(unittest.TestCase):
    def test_player(self):
        player = Player("test")
        self.assertEqual(player.name, "test")


if __name__ == "__main__":
    unittest.main()
