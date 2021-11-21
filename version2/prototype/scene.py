import sys

class IScene:
    def __init__(self) -> None:
        pass


    def update(self):
        print("Updated")


class Title(IScene):
    pass



if __name__ == "__main__":
    scene = Title()
    scene.update()
