
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
        ability: Ability
        for ability in self.abilities:
            if ability_name == ability.name:
                return ability
        return



actor = Actor()
actor.setAbility(Ability("FireBall"))
actor.setAbility(Ability("IceBall"))

actor.getAbility("FireBall").execute()