print("Battle")
# a-a

class DefaultClass:
    def __init__(self) -> None:
        print(self.__class__.__name__)

class ClassA:
    def __init__(self) -> None:
        print(self.__class__.__name__)


class_dict = {
    "classa": ClassA
}
className = input("> ").lower()
cls = class_dict.get(className, DefaultClass)

cls()

