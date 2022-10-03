

class UserMemento:
    mementos = []
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.mementos.append(self)

class User:
    def __init__(self, name, age) -> None:
        self._name = name
        self._age = age

    def changeName(self, name):
        self._name = name

    def createMemento(self):
        return UserMemento(self._name, self._age)

    def restoreMemento(self, memento: UserMemento):
        self._name = memento.name
        self._age = memento.age

    @property
    def name(self):
        return self._name


user = User("Alice", 17)
memento = user.createMemento()
print(user.name)
user.changeName("Bob")
print(user.name)
memento2 = user.createMemento()
user.restoreMemento(memento)
print(user.name)
user.restoreMemento(memento2)
print(user.name)

print(UserMemento.mementos)