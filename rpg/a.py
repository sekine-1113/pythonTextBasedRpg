
class BaseItem:
    def __init__(self, name: str, price: int) -> None:
        self.name = name
        self.price = price


class Item(BaseItem):
    def __init__(self, name: str, price: int) -> None:
        super().__init__(name, price)

    def show(self) -> None:
        print(self.name)
        print(self.price)

    def clone(self) -> "Item":
        return Item(self.name, self.price)



if __name__ == "__main__":

    item = Item("やくそう", 8)
    item2 = item.clone()

    print(item.name, item2.name)

    item.name = "上やくそう"

    print(item.name, item2.name)