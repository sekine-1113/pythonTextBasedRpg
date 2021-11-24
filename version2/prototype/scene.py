import sys

class IScene:
    def __init__(self, prev_scene: "IScene"=None) -> None:
        self.__prev_scene = prev_scene

    def update(self):
        print("Updated")

    def run(self):
        pass


class Title(IScene):
    def run(self):
        print("TextBasedRPG")
        print("============")
        print("1. Start")
        print("2. Exit")
        print("3. Config")
        command = int(input("> "))
        match command:
            case 1:
                print("Start")
            case 2:
                print("Exit")
            case 3:
                print("Config")
            case _:
                print("?")




if __name__ == "__main__":
    scene = Title()
    scene.run()
    scene.update()
