

class ValueObject:
    value = None
    def __init__(self, value) -> None:
        self.value = value

    def __setattr__(self, __name: str, __value) -> None:
        if self.value is None:
            super().__setattr__(__name, __value)
        else:
            raise Exception


class UserName(ValueObject):
    def __init__(self, user_name) -> None:
        super().__init__(user_name)

    @property
    def get(self):
        return self.value

    def change(self, user_name) -> "UserName":
        return UserName(user_name)


user = UserName("Alice")

print(user.get)

user = user.change("Bob")

print(user.get)