DEFAULT_PROMPT = "> "
DEFAULT_MIN = 0
DEFAULT_MAX = 0
DEFAULT_ARRAY = []


def integer(prompt: str=DEFAULT_PROMPT) -> int:
    user_input = input(prompt)
    try:
        user_input = int(user_input)
        return user_input
    except ValueError as e:
        return integer(prompt)


def integer_within_range(prompt: str=DEFAULT_PROMPT, _min: int=DEFAULT_MIN, _max: int=DEFAULT_MAX) -> int:
    user_input = input(prompt)
    try:
        user_input = int(user_input)
        if _min <= user_input <= _max:
            return user_input
        return integer_within_range(prompt, _min, _max)
    except ValueError:
        return integer_within_range(prompt, _min, _max)


def integer_within_array(prompt: str=DEFAULT_PROMPT, _array: list=DEFAULT_ARRAY) -> int:
    user_input = input(prompt)
    try:
        user_input = int(user_input)
        if user_input in _array:
            return user_input
        return integer_within_array(prompt, _array)
    except ValueError:
        return integer_within_array(prompt, _array)


if __name__ == "__main__":
    integer("[1] OK [0] NG > ")

    integer_within_range("[1] OK [0] NG > ", 0, 1)
    integer_within_array("[1] OK [0] NG > ", [0, 1])
