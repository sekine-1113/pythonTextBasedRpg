import sys


class IScene:
    def __init__(self, prev_scene: "IScene"=None) -> None:
        self._prev_scene = prev_scene

    def update(self):
        print("Updated")



class NullScene(IScene):
    def __init__(self) -> None:
        pass

    def update(self):
        sys.exit(f"[call] {self.__class__.__name__}().update()")


class Title(IScene):
    def __init__(self) -> None:
        super().__init__(prev_scene=NullScene())

    def update(self):
        print("TextBasedRPG")
        print("============")
        print("1. Start")
        print("2. Exit")
        print("3. Config")
        command = int(input("> "))
        match command:
            case 1:
                return MyPage()
            case 2:
                return self._prev_scene
            case 3: print("Config")
            case _:
                return NullScene()


class MyPage(IScene):
    def __init__(self) -> None:
        super().__init__(prev_scene=Title())

    def update(self):
        print("MyPage")
        print("============")
        print("1. Start")
        print("2. Back")
        command = int(input("> "))
        match command:
            case 1:
                return NullScene()
            case 2:
                return self._prev_scene
            case _:
                return NullScene()



if __name__ == "__main__":
    scene = Title()
    while scene:
        scene = scene.update()