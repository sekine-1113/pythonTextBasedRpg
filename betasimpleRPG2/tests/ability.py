
class Ability:
    def __init__(self, name) -> None:
        self.name = name

    def __repr__(self) -> str:
        return self.name

    def execute(self):
        print("Execute:", self.name)


class Actor:
    def __init__(self) -> None:
        self.abilities = []

    def setAbility(self, ability):
        self.abilities.append(ability)

    def getAbility(self, ability_name) -> Ability:
        return list(
            filter(
                (lambda x: ability_name == x.name),
                self.abilities
            )
        )[0]



actor = Actor()
actor.setAbility(Ability("FireBall"))
actor.setAbility(Ability("IceBall"))

actor.getAbility("FireBall").execute()
actor.getAbility("IceBall").execute()

print(actor.abilities)