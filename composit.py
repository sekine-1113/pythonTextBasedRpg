

class CompositObject:
    def __init__(self, name) -> None:
        self.name = name
        self.parent = None
        self.path = ""
        self.spi = "\\"

class Dirctory(CompositObject):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.children = []

    def add(self, _object: CompositObject):
        _object.parent = self
        if self.parent:
            _object.path = self.parent.name + self.spi
        _object.path += self.name + self.spi + _object.name
        self.children.append(_object)

    def input_command(self):
        command = input(f"{self.path}>")
        if command == "cd":
            return self.change(input("path?>"))
        return


    def change(self, path: str):
        print("cd", path)
        if path.startswith(".."):
            if self.parent:
                return self.parent
        elif path.startswith("."):
            return self
        else:
            for child in self.children:
                if isinstance(child, Dirctory):
                    if child.name == path:
                        return child
            return self

    def show(self):
        for child in self.children:
            if isinstance(child, File):
                child.show()
            else:
                print(child.path)

    def __repr__(self) -> str:
        return f"{self.path}"

class File(CompositObject):
    def __init__(self, name) -> None:
        super().__init__(name)

    def show(self):
        print(self.path)

    def __repr__(self) -> str:
        return f"{self.path}"

def main():
    current = Dirctory("C:")
    current.path = "C:"
    current.add(Dirctory("temp"))
    current.add(File("temp.py"))
    current.show()
    current = current.change("temp")
    current.add(File("some.py"))
    current.show()
    current = current.change("..")
    current.show()
    current = current.change("temp")
    current.add(Dirctory("sub"))
    current.add(Dirctory("third"))
    current = current.change("sub")
    current.add(File("main.py"))

    current = current.change("..")
    print(current.path+">")
    current.show()



if __name__ == "__main__":
    main()