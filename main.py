# import webbrowser
# url = r"index.html"
# webbrowser.open(url)


class PlayerModel:
    def __init__(self, name) -> None:
        self.name = name

    def get_name(self):
        return self.name


class PlayerView:
    def __init__(self) -> None:
        pass

    def display_name(self, name):
        print("name:", name)

    def ask_get_name(self):
        return input("Get Name? > ")



class PlayerController:
    def __init__(self, pmodel: PlayerModel, pview: PlayerView) -> None:
        self.model = pmodel
        self.view = pview

    def get_name(self):
        cmd = self.view.ask_get_name()
        if cmd.lower() in ("y", "yes"):
            name = self.model.get_name()
            self.view.display_name(name)


if __name__ == "__main__":
    c = PlayerController(
            PlayerModel("アリス"),
            PlayerView()
        )
    c.get_name()