from abc import ABC


class Buffer:
    def __init__(self) -> None:
        self._messages = []

    def add_message(self, message):
        self._messages.append(message)

    def remove_message(self, message):
        self._messages.remove(message)

    def print(self):
        for o in self._messages[:]:
            o.print()
            self.remove_message(o)


class Message(ABC):
    def __init__(self) -> None:
        pass

    def print(self):
        pass

class A(Message):
    def print(self):
        print("This is a class A! ;)")

class B(Message):
    def print(self):
        print("This is a class B! ;)")

buff = Buffer()
buff.add_message(A())
buff.add_message(B())
buff.print()
"""
This is a class A! ;)
This is a class B! ;)
"""

