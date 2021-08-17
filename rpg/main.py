import unittest


class Player:
    def __init__(self, name) -> None:
        self.name = name


class TestPlayer(unittest.TestCase):
    """test class of tashizan
    """

    def test_player(self):
        """test method for tashizan
        """
        player_name = "Bob"
        player = Player(player_name)
        name = "Bob"
        self.assertEqual(player.name, name)


if __name__ == "__main__":
    unittest.main()