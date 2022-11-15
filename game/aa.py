import unittest


class HPObject:
    def __init__(self, value) -> None:
        self.value = max(0, value)

    def add(self, x):
        if x < 0:
            raise ValueError
        return HPObject(self.value + x)

    def sub(self, x):
        if x < 0:
            raise ValueError
        return HPObject(self.value - x)

    def __repr__(self) -> str:
        return f"<class: {self.__class__.__name__}, value: {self.value}>"

    def __str__(self) -> str:
        return str(self.value)


class TestHPObject(unittest.TestCase):
    def test_init(self):
        self.assertEqual(HPObject(0).value, 0)


    def test_add(self):
        self.assertEqual(HPObject(0).add(100).value, 100)

    def test_add_exception(self):
        with self.assertRaises(ValueError):
            HPObject(0).add(-100)

    def test_sub(self):
        self.assertEqual(HPObject(200).sub(100).value, 100)

    def test_sub_exception(self):
        with self.assertRaises(ValueError):
            HPObject(0).sub(-100)

class Player:
    def __init__(self, name, HP, ATK) -> None:
        self.name = name or ""
        if not isinstance(HP, HPObject) and isinstance(HP, int):
            if HP < 0:
                raise ValueError
            HP = HPObject(HP)
        self.HP = HP
        self.ATK = ATK or 0

    def attack(self):
        return self.ATK

    def recieve(self, damage):
        newHP = self.HP.sub(damage)
        return Player(self.name, newHP, self.ATK)

    def is_dead(self):
        return self.HP.value == 0

    def save(self):
        return self.__dict__


def t():
    p1 = Player("nameA", 300, 120)
    s1 = p1.save()
    print(s1)
    p2 = Player("nameB", HPObject(280), 140)

    d1 = p1.attack()
    p2 = p2.recieve(d1)
    p2 = p2.recieve(d1)
    p2 = p2.recieve(d1)
    s = p2.save()
    print(s)
    print(str(s["HP"]))
    print(p2.is_dead())


if __name__ == "__main__":
    unittest.main()