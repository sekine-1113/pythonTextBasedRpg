
class Dictable:

    def asdict(self):
        r = {}
        for k, v in vars(self).items():
            if isinstance(v, Dictable):
                v = v.asdict()
            if isinstance(v, list|tuple|set):
                v2 = []
                for v1 in v:
                    if isinstance(v1, Dictable):
                        v2.append(v1.asdict())
                    else:
                        v2.append(v1)
                v = v2
            r[k] = v
        return r


class Item(Dictable):
    def __init__(self, name) -> None:
        self.name = name


class ItemList(Dictable):
    def __init__(self, *items: list[Item]) -> None:
        self.items = items

if __name__ == "__main__":
    items = [
        Item("アイテムA"),
        Item("アイテムB")
    ]

    print(ItemList(Item("アイテムC"), Item("アイテムD"), *items).asdict())
