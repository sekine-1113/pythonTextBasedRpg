
def message(message_text):
    print(message_text)
    return message_text


def attack_message(actor, action):
    print("[INFO:attack_message] ", end="")
    print(actor.name, action.name)
    return True


if __name__ == "__main__":
    from cui.textbasedrpg.sample.game.game import Actor, Skill
    test_actor = Actor("test", 1, 30, 10, 10, 10, 0, 0)
    test_skill = Skill("Fire", 10)
    test_actor.set_render(attack_message)
    message("test")
    test_actor.attack(test_skill)
