import unittest

from games.cui.textbasedrpg.version2.data.item import Item


class TestItem(unittest.TestCase):

    def test_item_ok(self):
        item = Item(0, "なし", "なし")
        self.assertEqual(item.id, 0)
        self.assertEqual(item.name, "なし")
        self.assertEqual(item.explain, "なし")

    def test_item_ng(self):
        item = Item(0, "なし", "なし")
        self.assertNotEqual(item.id, 1)
        self.assertNotEqual(item.name, "ほげ")
        self.assertNotEqual(item.explain, "ふが")


if __name__ == "__main__":
    unittest.main()
