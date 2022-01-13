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

class IObject:
    def create(self):
        pass

class Milk(IObject):
    def create(self):
        return "Milk"

class Choco(IObject):
    def create(self):
        return "Choco"

class Factory(Singleton):
    def create(self, _object: IObject):
        return _object.create()

class TestFactory(unittest.TestCase):
    def test_main(self):
        factory = Factory()
        self.assertEqual(factory.create(Milk()), "Milk")
        self.assertEqual(factory.create(Choco()), "Choco")


class Prototype:
    def clone(self):
        return deepcopy(self)


class TestPrototype(unittest.TestCase):
    def test_main(self):
        class Animal(Prototype):
            def __init__(self, name) -> None:
                self.name = name
        animal = Animal("Pochi")
        animal_clone = animal.clone()
        self.assertEqual(animal.name, animal_clone.name)


if __name__ == "__main__":
    unittest.main()
