
class Item:
    def __init__(self, name):
        self.name = name


class ItemFactory:

    def __init__(self):
        self.pool = {}

    def create(self, name):
        if self.pool.get(name):
            print("registed")
            return self.pool.get(name)

        self.pool[name] = Item(name)
        return self.pool[name]


class Inventory:

    def __init__(self):
        self.inv = {}

    def add_item(self, item, count):
        if self.inv.get(item.name):
            self.inv[item.name]["count"] += count
            return self.inv[item.name]

        self.inv[item.name] = {
            "name": item.name,
            "count": count,
        }

        return self.inv[item.name]


if __name__ == "__main__":
    inv = Inventory()
    factory = ItemFactory()
    i1 = factory.create("yakusou")
    result = inv.add_item(i1, 1)
    print(result)
    i2 = factory.create("yakusou")
    result = inv.add_item(i2, 3)
    print(result)
