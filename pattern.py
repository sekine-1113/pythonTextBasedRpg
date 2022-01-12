import unittest
from copy import deepcopy


class Singleton:
    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(Singleton, cls).__new__(cls)
        return cls.__instance

    def get_instance(self):
        return self.__instance


class TestSingleton(unittest.TestCase):
    def test_main(self):
        class MyClass(Singleton):
            def __init__(self, name) -> None:
                self.name = name
        alice = MyClass("Alice")
        bob = MyClass("Bob")
        self.assertEqual(alice, bob)


class FactoryType:
    MILK= 0
    CHOCO = 1


class Factory(Singleton):
    def create(self, _type: FactoryType):
        match _type:
            case FactoryType.MILK:
                return "Milk"
            case FactoryType.CHOCO:
                return "Choco"
            case _:
                return "null"


class TestFactory(unittest.TestCase):
    def test_main(self):
        factory = Factory()
        self.assertEqual(factory.create(FactoryType.MILK), "Milk")
        self.assertEqual(factory.create(FactoryType.CHOCO), "Choco")


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


def mylogging(logger=None):
    from datetime import datetime
    def wrapper(func):
        def inner(*args, **kwargs):
            tm = datetime.today().now().strftime("%Y-%m-%d %H:%M:%S")
            fn_name = func.__name__
            _args = ",".join(args) if args else ""
            _kwargs = ",".join(["=".join(map(str, item)) for item in kwargs.items()]) if kwargs else ""
            msg = f"[{tm}] {fn_name} called"
            logger.debug(msg)
            logger.debug(f"args:{_args}\nkwargs:{_kwargs}")
            obj = func(*args, **kwargs)
            logger.debug("finish")
            return obj
        return inner
    return wrapper


if __name__ == "__main__":
    unittest.main()
