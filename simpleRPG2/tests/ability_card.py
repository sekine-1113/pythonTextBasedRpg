
import random


class AbilityCard:
    def __init__(self, name, cost, effect, description):
        self.name = name
        self.cost = cost
        self.effect = effect
        self.description = description

    def __str__(self):
        return f"{self.name}#{self.cost}<{self.description}>"

    def __repr__(self):
        return self.__str__


class AbilityDeck:
    def __init__(self, cards = []):
        self.cards = cards
        self.__trushes = []

    def rebuild(self, n=0):
        if n==0:
            self.cards.extend(self.__trushes)
            self.__trushes.clear()
        else:
            for _ in range(n):
                self.cards.append(self.__trushes.pop())


    def draw(self):
        card = self.cards.pop()
        self.__trushes.append(card)
        print("Draw: "+ str(card), "@",self.length())
        return card

    def shuffle(self):
        random.shuffle(self.cards)
        print("=== shuffled ===")

    def show(self):
        print(*self.cards)

    def length(self):
        return len(self.cards)



cards = []
for i in range(10):
    cards.append( AbilityCard(**{"name": f"A{i}", "cost": random.randint(1, 10), "effect": None, "description": f"A{i}"}) )
deck = AbilityDeck(cards)
deck.shuffle()
deck.show()
deck.draw()
deck.draw()
deck.draw()
deck.draw()
deck.rebuild(2)
print(deck.length())
deck.show()
deck.rebuild(2)
deck.show()