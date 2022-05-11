

class CompositObject:
    def __init__(self, name) -> None:
        self.name = name
        self.parent = None

class Dirctory(CompositObject):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.children = []

    def add(self, _object):
        self.children.append(_object)

class File(CompositObject):
    def __init__(self, name) -> None:
        super().__init__(name)


root = Dirctory("root")
print(root.children)
root.add(File("test.txt"))