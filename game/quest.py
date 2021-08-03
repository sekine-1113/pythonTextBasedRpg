
"""
Quests ->
    Quest No. 1 to 5
        Quest No.1: Lv 1 to Lv 5
        Quest No.2: Lv 6 to Lv 10
        ...
    Quest No. 6 to 10
        Quest No.6: Lv 26 to 30
        ...
    ...
"""

quests_data = {
    "1to5": {
        "id": 1,
        "title": "Defeat Slime",
        "description": "Defeat slime",
        "reward": {"Herb": 0.8, "Good Herb": 0.2}
    },
    "6to10": {
        "id": 2,
        "title": "Defeat Goblin",
        "description": "Defeat goblin",
        "reward": {"Herb": 0.85, "Good Herb": 0.15}
    }
}

class Quest:
    def __init__(self, id, title, description, reward) -> None:
        self.id = id
        self.title = title
        self.desc = description
        self.reward = reward

    def __repr__(self) -> str:
        return f"{self.id=} {self.title=} {self.desc=} {self.reward=}"
