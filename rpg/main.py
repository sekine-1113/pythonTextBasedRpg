

class Tag:
    def __init__(self, _id, name) -> None:
        self._id = _id
        self.name = name

    def __repr__(self) -> str:
        return f"[{self._id} {self.name}]"


class TagList:
    def __init__(self, _list) -> None:
        self._list = _list

    def getByName(self, name):
        for n in self._list:
            if n.name == name:
                print("Find")
                return n
        print("Not found.")

    def getById(self, _id):
        for n in self._list:
            if n._id == _id:
                print("Find")
                return n
        print("Not found.")


tags = [
    Tag(0, "タグ1"),
    Tag(1, "タグ2"),
    Tag(2, "タグ3"),
]

tl = TagList(tags)

t = tl.getById(2)
print(t)

"""to be continuted
"""