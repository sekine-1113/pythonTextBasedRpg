print("Battle")
# a-a

class DefaultClass:
    def __init__(self, **obj) -> None:
        print(self.__class__.__name__)
        self.obj = obj

class ClassA:
    def __init__(self, **obj) -> None:
        print(self.__class__.__name__)
        self.obj = obj


class_dict = {
    "classa": ClassA
}
className = input("> ").lower()
cls = class_dict.get(className, DefaultClass)
obj = {}
cls(**obj)

