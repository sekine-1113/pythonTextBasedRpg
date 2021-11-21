
class Game():
    def run(self):
        print(self.__class__.__name__)


if __name__ == "__main__":
    game = Game()
    game.run()