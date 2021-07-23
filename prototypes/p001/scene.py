from copy import deepcopy


class Memento(object):

    def __init__(self, state) -> None:
        self.__state = state

    @property
    def state(self):
        return self.__state

    def __repr__(self) -> str:
        return f"{self.state}"


class Originator(object):

    def commit(self):
        return Memento(deepcopy(self.__dict__))

    def rollback(self, memento):
        self.__dict__ = memento.state


class Cat(Originator):
    def __init__(self, name) -> None:
        self.name = name


cat = Cat("Tom")
print(cat.name)
cat_memento = cat.commit()
cat.name = "jerry"
print(cat.name)
cat.rollback(cat_memento)
print(cat.name)
