import random

from ability import AbilityEntity
from actor import ActorEntity


class EnemyAbilityAI:
    def __init__(self, source: ActorEntity, abilities: list[AbilityEntity]):
        self.source = source
        self.abilities = abilities

    def select(self) -> AbilityEntity:
        ability: AbilityEntity
        abilities: list[AbilityEntity] = []
        for ability in self.abilities:
            if ability.can_use():
                abilities.append(ability)
        probs = []
        p = 100/len(abilities)
        for ability in abilities:
            if (self.source.hitpoint / self.source.max_hitpoint) < 0.5:
                if ability.type_ == 1:  # heal
                    p *= 2
            probs.append(p)
        return random.choices(abilities, probs, k=1)[0]

    def get_index(self, ability: AbilityEntity) -> int:
        return self.abilities.index(ability)


class Enemy:
    def __init__(self, cur, idx) -> None:
        self.cur = cur
        self.idx = idx

    def get_status(self) -> tuple:
        status = self.cur.execute(
            "SELECT hitpoint, strength, defence, magicpower, critical FROM enemies_master WHERE id=?", (self.idx, )).fetchall()[0]
        return status

    def get_abilities(self) -> list[AbilityEntity]:
        abilities = self.cur.execute(
            """
            SELECT ability.name, ability.description, ability.count, ability.target, ability.type, ability.fixed_value, ability.value
            FROM ability
            JOIN (SELECT ability_id FROM enemies_master WHERE id=?) as em
            WHERE ability.id=em.ability_id
            """, (self.idx, )
        ).fetchall()
        for i, ability in enumerate(abilities):
            abilities[i] = AbilityEntity(*ability)
        return abilities

    def get_exp(self) -> int:
        exp = self.cur.execute("SELECT exp FROM enemies_master WHERE id=?", (self.idx,)).fetchone()[0]
        return exp

    def get_name(self) -> str:
        return self.cur.execute("SELECT name FROM enemies_master WHERE id=?", (self.idx,)).fetchone()[0]

    def get_entity(self) -> ActorEntity:
        entity = ActorEntity(*self.get_status())
        entity.set_abilities(self.get_abilities())
        entity.set_enemy_ai(EnemyAbilityAI(entity, self.get_abilities()))
        return entity


class EnemyFactory:
    def __init__(self, cur) -> None:
        self.cur = cur

    def create(self, idx: int) -> Enemy:
        enemy = Enemy(self.cur, idx)
        return enemy
