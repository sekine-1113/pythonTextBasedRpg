import unittest
from copy import deepcopy

from pattern.singleton import Singleton


class TestSingleton(unittest.TestCase):
    def test_main(self):
        class MyClass(Singleton):
            def __init__(self, name) -> None:
                self.name = name
        alice = MyClass("Alice")
        bob = MyClass("Bob")
        self.assertEqual(alice, bob)


if __name__ == "__main__":
    unittest.main()
