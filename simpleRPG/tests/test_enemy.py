import unittest

from games.cui.textbasedrpg.simpleRPG.classes.enemy import MockEnemy


class TestEnemy(unittest.TestCase):
    def test_enemy(self):
        enemy = MockEnemy()
        self.assertEqual(enemy.name, "Mock")

    def test_get_parameters(self):
        enemy = MockEnemy()
        self.assertEqual(enemy.get_parameters(), None)


if __name__ == "__main__":
    unittest.main()
