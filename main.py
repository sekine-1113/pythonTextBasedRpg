from utils.windows import Color, unlock_ansi

unlock_ansi()


class Printer:
    def __init__(self, color=None) -> None:
        self.color = color

    def __enter__(self):
        if self.color is None:
            return self
        print(self.color, end="")
        return self

    def red(self, txt,  **kwargs):
        print(Color.RED+txt, **kwargs)
        return self

    def green(self, txt, **kwargs):
        print(Color.GREEN+txt, **kwargs)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print(Color.RESET, end="")


with Printer() as p:
    p.red("Hello", end="").green("World")