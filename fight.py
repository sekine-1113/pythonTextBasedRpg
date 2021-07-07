
class Fight:

    def __init__(self, recoverable=True, item_usable=True, turn_limit=999) -> None:
        self.recoverable = recoverable
        self.item_usable = item_usable
        self.turn_limit = turn_limit

    def run(self, player: object, enemy: object):
        pass