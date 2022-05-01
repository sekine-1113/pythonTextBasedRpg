def integer(prompt:str="> ") -> int:
    user_input = input(prompt)
    try:
        user_input = int(user_input)
        return user_input
    except ValueError:
        return integer(prompt)