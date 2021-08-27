from abc import ABC, abstractmethod


class Printer(ABC):
    @abstractmethod
    def print_(self):
        ...


class ConsolePrinter(Printer):
    def __init__(self) -> None:
        super().__init__()

    def print_(self, *args):
        print(*args)


class FilePrinter(Printer):
    def __init__(self, fp) -> None:
        super().__init__()
        self.fp = fp

    def print_(self, *args):
        with open(self.fp, "w", encoding="utf-8") as f:
            f.write(*args)



class Notify:
    def __init__(self, printer: Printer) -> None:
        self.printer = printer

    def print_(self, *args):
        self.printer.print_(*args)


notify = Notify(FilePrinter(r"D:\myscript\games\cui\textbasedrpg\rpg\test.txt"))
notify.print_("Hello")