
class BaseItem:
    def __init__(self, name: str, price: int, _id: int) -> None:
        self.name = name
        self.price = price
        self._id = _id


class Item(BaseItem):
    def __init__(self, name: str, price: int, _id: int) -> None:
        super().__init__(name, price, _id)

    def show(self) -> None:
        print(self._id, self.name)
        print(self.price)

    def clone(self) -> "Item":
        return Item(self.name, self.price, self._id)

    def __repr__(self) -> str:
        return f"{self._id}: {self.name}"


class ItemList:
    def __init__(self) -> None:
        self.strage = []

    def add(self, item: Item) -> None:
        self.strage.append(item)

    def remove(self, item: Item) -> None:
        self.strage.remove(item)

    def show(self) -> None:
        for strage in self.strage:
            print(strage)

    def sort(self, key: object=None, reverse: bool=False) -> None:
        if key is None:
            key = lambda x: x._id
        self.strage.sort(key=key, reverse=reverse)


if __name__ == "__main__":

    item = Item("やくそう", 8, 1)
    item2 = item.clone()

    item.name = "上やくそう"
    item._id = 2

    item_list = ItemList()
    item_list.add(item)
    item_list.add(item2)

    item_list.show()

    print("===========")
    item_list.sort()

    item_list.show()
    print("===========")

    item_list.remove(item)

    item_list.show()
