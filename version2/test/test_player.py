import unittest

from games.cui.textbasedrpg.version2.data.player import Player


class TestPlayer(unittest.TestCase):
    def test_player_ok(self):
        player = Player("テスト", 0, 0)
        self.assertEqual(player.name, "テスト")
        self.assertEqual(player.money, 0)
        self.assertEqual(player.job_id, 0)

    def test_player_ng(self):
        player = Player("テスト", 0, 0)
        self.assertNotEqual(player.name, "テストNG")
        self.assertNotEqual(player.money, -1)
        self.assertNotEqual(player.job_id, -1)

if __name__ == "__main__":
    unittest.main()