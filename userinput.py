
class Input:
    def __init__(self) -> None:
        super().__init__()


    def integer(self, prompt:str="> ") -> int:
        user_input = input(prompt)
        try:
            user_input = int(user_input)
            return user_input
        except ValueError as e:
            return self.integer(prompt)

    def integer_with_range(self, prompt:str="> ", _min:int=0, _max:int=0) -> int:
        user_input = input(prompt)
        try:
            user_input = int(user_input)
            if _min <= user_input <= _max:
                return user_input
            return self.integer_with_range(prompt, _min, _max)
        except ValueError:
            return self.integer_with_range(prompt, _min, _max)

    def integer_with_array(self, prompt:str="> ", _array:list=[]) -> int:
        user_input = input(prompt)
        try:
            user_input = int(user_input)
            if user_input in _array:
                return user_input
            return self.integer_with_array(prompt, _array)
        except ValueError:
            return self.integer_with_array(prompt, _array)


if __name__ == "__main__":
    user_input = Input()
    user_input.integer("[1] OK [0] NG > ")

    user_input.integer_with_range("[1] OK [0] NG > ", 0, 1)
    user_input.integer_with_array("[1] OK [0] NG > ", [0, 1])
