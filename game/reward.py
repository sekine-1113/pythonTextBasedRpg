class Reward:
    def __init__(self, reward_xp, reward_item) -> None:
        self.xp = reward_xp
        self.item = reward_item


class Quest:
    def __init__(self, name, reward) -> None:
        self.name = name
        self.reward = reward


