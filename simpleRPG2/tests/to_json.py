import json
from copy import copy


class tojson:
    unsupported = (
        complex,
        bytes,
        bytearray,
        memoryview,
        range
    )

    def __new__(cls, _class, include_class_name=True) -> dict:
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
        for varname, value in class_vars.items():
            if value.__class__ in cls.unsupported:
                continue
            if value is not None:
                func = cls._funcs.get(value.__class__, cls._fromclass)
                value = func(value)
            class_vars[varname] = value
        if include_class_name:
            class_vars = {_class.__class__.__name__: class_vars}
        return json.loads(json.dumps(class_vars))

    @classmethod
    def _fromint(cls, value):
        return value

    @classmethod
    def _fromfloat(cls,value):
        return value

    @classmethod
    def _fromstr(cls,value):
        return value

    @classmethod
    def _frombool(cls,value):
        return value

    @classmethod
    def _fromlist(cls, value):
        cp = copy(value)
        for i, item in enumerate(cp):
            func = cls._funcs.get(item.__class__, cls._fromclass)
            cp[i] = func(item)
        return cp

    @classmethod
    def _fromtuple(cls,value):
        return cls._fromlist(list(value))

    @classmethod
    def _fromdict(cls, value):
        cp = copy(value)
        for varname, val in cp.items():
            func = cls._funcs.get(val.__class__, cls._fromclass)
            cp[varname] = func(val)
        return cp

    @classmethod
    def _fromclass(cls, value):
        return cls.__new__(cls, value)

    @classmethod
    def _fromset(cls, value):
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
        self.data = users


print(
    json.dumps(
        tojson(
            Users(
                users=[
                    User(name="Alice", age=27, items=[Item(name="iPhone12")]),
                    User(name="Bob", age=30, items=[Item(name="iPhone8"),Item(name="iPhone10")])
                ]
            )
        ),
    )
)

"""
{"Users":
    {"data": [
            {"User": {"name": "Alice", "age": 27, "items": [{"Item": {"name": "iPhone12"}}]}},
            {"User": {"name": "Bob", "age": 30, "items": [{"Item": {"name": "iPhone8"}}, {"Item": {"name": "iPhone10"}}]}}
        ]
    }
}
"""