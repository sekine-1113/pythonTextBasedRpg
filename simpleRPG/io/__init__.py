import json


def integer(prompt:str="> ") -> int:
    user_input = input(prompt)
    try:
        user_input = int(user_input)
        return user_input
    except ValueError as e:
        return integer(prompt)

def integer_within_range(prompt:str="> ", _min:int=0, _max:int=0) -> int:
    user_input = input(prompt)
    try:
        user_input = int(user_input)
        if _min <= user_input <= _max:
            return user_input
        return integer_within_range(prompt, _min, _max)
    except ValueError:
        return integer_within_range(prompt, _min, _max)

def integer_within_array(prompt:str="> ", _array:list=[]) -> int:
    user_input = input(prompt)
    try:
        user_input = int(user_input)
        if user_input in _array:
            return user_input
        return integer_within_array(prompt, _array)
    except ValueError:
        return integer_within_array(prompt, _array)

def output(*args, **kwargs) -> None:
    print(*args, **kwargs)