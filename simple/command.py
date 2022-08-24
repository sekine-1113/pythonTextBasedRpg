
class Command:
    pass

class MenuItem:
    def __init__(self, name) -> None:
        self.name = name

class Menu:
    def __init__(self, name) -> None:
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)

if __name__ == "__main__":
    pass

