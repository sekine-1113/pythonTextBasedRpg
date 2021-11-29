from utils.windows import Color, unlock_ansi

unlock_ansi()

print(f"{Color.BLUE}[RED]{Color.RESET}")

class Printer:
    def __init__(self, color) -> None:
        self.color = color

    def __enter__(self):
        if self.color is None:
            return self
        print(self.color, end="")

    def __exit__(self, exc_type, exc_value, traceback):
        print(Color.RESET, end="")


with Printer(Color.RED) as p:
    print("Hello")