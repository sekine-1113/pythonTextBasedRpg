import json
from copy import copy


class tojson:
    unsupported = (
        complex,
        bytes,
        bytearray,
        memoryview,
        range,
    )

    def __new__(cls, _class) -> dict:
        cls._funcs = {
            int: cls._fromint,
            float: cls._fromfloat,
            bool: cls._frombool,
            str: cls._fromstr,
            list: cls._fromlist,
            tuple: cls._fromtuple,
            dict: cls._fromdict,
            set: cls._fromset,
        }

        class_vars = copy(_class.__dict__)
        varname: str
        for varname, value in class_vars.items():
            if value.__class__ in cls.unsupported:
                continue
            if value is not None:
                func = cls._funcs.get(value.__class__, cls._fromclass)
                value = func(value)
            class_vars[varname] = value
        return json.loads(json.dumps(class_vars))

    @classmethod
    def _fromint(cls, value: int) -> int:
        return value

    @classmethod
    def _fromfloat(cls, value: float) -> float:
        return value

    @classmethod
    def _fromstr(cls, value: str) -> str:
        return value

    @classmethod
    def _frombool(cls, value: bool) -> bool:
        return value

    @classmethod
    def _fromlist(cls, value: list) -> list:
        cp = copy(value)
        for i, item in enumerate(cp):
            if item.__class__ in cls.unsupported:
                continue
            func = cls._funcs.get(item.__class__, cls._fromclass)
            cp[i] = func(item)
        return cp

    @classmethod
    def _fromtuple(cls, value: tuple) -> list:
        return cls._fromlist(list(value))

    @classmethod
    def _fromdict(cls, value: dict) -> dict:
        cp = copy(value)
        for varname, val in cp.items():
            if val.__class__ in cls.unsupported:
                continue
            func = cls._funcs.get(val.__class__, cls._fromclass)
            cp[varname] = func(val)
        return cp

    @classmethod
    def _fromclass(cls, value: object) -> dict:
        return cls.__new__(cls, value)

    @classmethod
    def _fromset(cls, value: set) -> list:
        return cls._fromlist(list(value))


class Item:
    def __init__(self, name) -> None:
        self.name = name

class User:
    def __init__(self, name, age, items) -> None:
        self.name = name
        self.age = age
        self.items = items


class Users:
    def __init__(self, users: list[User]) -> None:
        self.users = users

    def load(self, json_str: str) -> None:
        for user in json_str['users']:
            self.users.append(User(user['name'], user['age'], [Item(item['name']) for item in user['items']]))
        return self

def save(json_str: str, file: str, encoding: str="UTF-8"):
    with open(file, "w", encoding=encoding) as f:
        json.dump(json_str, f, indent=4)


def load(file, encoding: str="UTF-8"):
    with open(file, "r", encoding=encoding) as f:
        return json.load(f)


file = r"simpleRPG2\tests\test.json"

json_str = tojson(
    Users(
        users=[
            User(name="Alice", age=27, items=[Item(name="iPhone12")]),
            User(name="Bob", age=30, items=[Item(name="iPhone8"),Item(name="iPhone10")])
        ]
    )
)

save(json_str, file)
print(f"{json_str == tojson(Users([]).load(load(file))) = }")
"""
{"Users": [
        {"User": {"name": "Alice", "age": 27, "items": [{"Item": {"name": "iPhone12"}}]}},
        {"User": {"name": "Bob", "age": 30, "items": [{"Item": {"name": "iPhone8"}}, {"Item": {"name": "iPhone10"}}]}}
    ]
}
"""