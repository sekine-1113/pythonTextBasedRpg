"""
* Directory:
    * content[File, Directory]
    * name
    * path
    * parent
    * child

* File:
    * content[str]
    * name
    * path
    * parent
"""


class Entry:
    def __init__(self, name: str, content: object) -> None:
        self.name = name
        self.content = content
        self.path = None

    def set_path(self, path):
        self.path =  path + "/" + self.name

    def show(self):
        print(self.content)

    def __repr__(self) -> str:
        return f"{self.name=}"


class QuestLeaf(Entry):
    def __init__(self, name: str, content: str=None) -> None:
        super().__init__(name, content)
        self.path = self.name


class QuestNode(Entry):
    def __init__(self, name: str, content: list[Entry]=[]) -> None:
        super().__init__(name, content)
        self.path = self.name

    def add(self, entry: Entry) -> None:
        entry.set_path(self.path)
        self.content.append(entry)
        self.content.sort(key=lambda x: x.path)

    def show(self):
        for content in self.content:
            if isinstance(content, QuestNode):
                print(content.path)
            else:
                print(content.path)

    def find(self, path):
        for content in self.content:
            if content.name == path:
                return content
        print("Not found")
        return self


def main():
    root = QuestNode("Main")
    cwd = root
    cmd = ""
    while cmd != "exit":
        cmd = input(f"{cwd.name}> ")
        if cmd == "ls":
            cwd.show()
        elif cmd == "mkdir":
            name = input("> ")
            cwd.add(QuestNode(name))
        elif cmd == "mkfile":
            name = input("> ")
            content = input(">>> ")
            cwd.add(QuestLeaf(name, content))
        elif cmd == "cd":
            dr = input("> ")
            tmp = cwd.find(dr)
            if isinstance(tmp, QuestNode):
                cwd = tmp


if __name__ == "__main__":
    main()