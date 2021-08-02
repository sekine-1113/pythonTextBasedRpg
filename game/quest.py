
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

class Quests:
    def __init__(self) -> None:
        self.questList = []

    def add(self, questSeq):
        self.questList.append(questSeq)

class QuestList(list):
    pass

class Quest:
    def __init__(self, name, desc=None) -> None:
        self.name = name
        self.desc = desc

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self):
        return f"Quest {self.name}:'{self.desc}'"

qs = Quests()
ql = QuestList()
ql.append(Quest("No.1", "Slime"))
ql.append(Quest("No.2", "Goblin"))
ql.append(Quest("No.3", "Dragon"))
ql.append(Quest("No.4", "Demon"))
ql.append(Quest("No.5", "God"))
qs.add(ql)
ql2 = QuestList()
ql2.append(Quest("No.6", "Slime"))
ql2.append(Quest("No.7", "Goblin"))
ql2.append(Quest("No.8", "Dragon"))
ql2.append(Quest("No.9", "Demon"))
ql2.append(Quest("No.10", "God"))
qs.add(ql2)

for qls in qs.questList:
    for i in range(5):
        print(qls[i])
    print("="*23)