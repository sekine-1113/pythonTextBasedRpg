from games.cui.textbasedrpg.version2.prototype.scene import Title


class Game():
    def run(self):
        scene = Title()
        while scene:
            scene = scene.update()


if __name__ == "__main__":
    Game().run()
