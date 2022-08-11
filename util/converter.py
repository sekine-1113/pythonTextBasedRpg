import json
from copy import copy


class convertError(Exception):
    pass

class unSupportedError(Exception):
    pass

class tojson:
    """User-defined class convert to json

    Args:
    _class (object): instance of user-defined class

    Returns:
    dict: json object.
        bytes -> string\n
        bytearray -> string\n
        list, set, tuple -> json array

    Class Methods:
    `get_supported_classes` (tuple): tojson supported classes.
    `_from<type>` (<type>): convert from <type> to json object\n
    Examples:
    >>> tojson._fromint(123) == 123
    True
    >>> tojson._fromset({123, 456}) == [123, 456]
    True

    `_fromclass` (user-defined class): convert from instance of user-defined class to json object\n

    Examples:
    >>> class User:
    >>>    def __init__(self, name: str, age: int):
    >>>        self.name = name
    >>>        self.age = age

    >>> tojson._fromclass(User(name='Alice', age=20)) == {'name': 'Alice', 'age': 20}
    True
    """

    unsupported = (
        complex,
        memoryview,
    )

    def __new__(cls, _class=None, default_key="data") -> dict:
        cls._funcs = {
            int: cls._fromint,
            float: cls._fromfloat,
            bool: cls._frombool,
            str: cls._fromstr,
            list: cls._fromlist,
            tuple: cls._fromtuple,
            dict: cls._fromdict,
            set: cls._fromset,
            bytes: cls._frombytes,
            bytearray: cls._frombytearray,
        }

        if _class is None:
            return cls._funcs
        if not hasattr(_class, "__dict__"):
            class_vars: dict = copy(_class)
            if isinstance(_class, list|set|tuple):
                class_vars: dict = {default_key: cls._fromlist(_class)}
        else:
            class_vars: dict = copy(_class.__dict__)
        varname: str
        for varname, value in class_vars.items():
            if value.__class__ in cls.unsupported:
                print(value.__class__, "is unsupported. it converted to `str` object.")
                value = str(value)
            if value is not None:
                func = cls._funcs.get(value.__class__, cls._fromclass)
                value = func(value)
            class_vars[varname] = value
        result = json.loads(json.dumps(class_vars))
        return result

    @classmethod
    def get_supported_var_type(cls) -> tuple:
        """Gets the types of class variables supported by tojson.
        Returns: tuple
        """
        return tuple(tojson().keys())

    @classmethod
    def _fromint(cls, value: int) -> int:
        """Convert from int to json object.
        >>> tojson.fromint(123)
        123
        """
        return value

    @classmethod
    def _fromfloat(cls, value: float) -> float:
        """Convert from float to json object.
        >>> tojson.fromfloat(3.14)
        3.14
        """
        return value

    @classmethod
    def _fromstr(cls, value: str) -> str:
        """Convert from str to json object.
        >>> tojson.fromstr("Alice")
        Alice
        """
        return value

    @classmethod
    def _frombytes(cls, value: bytes) -> str:
        """Convert from bytes to json object.

        This is an implicit conversion from bytes to str

        >>> tojson.frombytes(b"Alice")
        Alice
        """
        return value.decode()

    @classmethod
    def _frombytearray(cls, value: bytearray) -> str:
        """Convert from bytes to json object.

        This is an implicit conversion from bytearray to str

        >>> tojson.frombytearray([97, 98, 99, 100, 101])
        abcde
        """
        return value.decode()

    @classmethod
    def _frombool(cls, value: bool) -> bool:
        """Convert from bool to json object.

        >>> tojson.frombool(True)
        True
        """
        return value

    @classmethod
    def _fromlist(cls, value: list) -> list:
        """Convert from list to json object.

        >>> tojson.fromlist(["Apple", "Banana", "Orange"])
        ['Apple', 'Banana', 'Orange']
        """
        cp = copy(value)
        for i, item in enumerate(cp):
            if item.__class__ in cls.unsupported:
                print(value.__class__, "is unsupported. it converted to `str` object.")
                item = str(item)
            func = tojson().get(item.__class__, cls._fromclass)
            cp[i] = func(item)
        return cp

    @classmethod
    def _fromtuple(cls, value: tuple) -> list:
        """Convert from tuple to json object.

        This is an implicit conversion from tuple to list.
        Equivalent to: `cls._fromlist(list(value))`

        >>> tojson.fromtuple(("Apple", "Banana", "Orange"))
        ['Apple', 'Banana', 'Orange']
        """
        return cls._fromlist(list(value))

    @classmethod
    def _fromdict(cls, value: dict) -> dict:
        """Convert from dict to json object.

        >>> tojson.fromdict({"name": "Alice", "age": 20})
        {'name': 'Alice', 'age': 20}
        """
        cp = copy(value)
        for varname, val in cp.items():
            if val.__class__ in cls.unsupported:
                print(value.__class__, "is unsupported. it converted to `str` object.")
                val = str(val)
            func = tojson().get(val.__class__, cls._fromclass)
            cp[varname] = func(val)
        return cp

    @classmethod
    def _fromclass(cls, value: object) -> dict:
        """ Convert from user-defined class to json object.

        Equivalent to: `tojson(value)`

        >>> class User:
        >>>     def __init__(self, name):
        >>>         self.name = name
        >>> tojson.fromclass(User("Alice"))
        {'name': 'Alice'}
        """
        return cls.__new__(cls, value)

    @classmethod
    def _fromset(cls, value: set) -> list:
        """Convert from set to json object.

        This is an implicit conversion from set to list.
        Equivalent to: `cls._fromlist(list(value))`

        >>> tojson.fromset({"Apple", "Banana", "Orange"})
        ['Apple', 'Banana', 'Orange']
        """
        return cls._fromlist(list(value))



if __name__ == "__main__":
    assert tojson._fromint(123) == 123
    assert tojson._fromfloat(3.14) == 3.14
    assert tojson._frombool(True) == True
    assert tojson._fromstr("Alice") == "Alice"
    assert tojson._fromtuple((1, 2, 3)) == [1, 2, 3]
    assert tojson._fromlist([1, 2, 3]) == [1, 2, 3]
    assert tojson._fromset({1, 2, 3}) == [1, 2, 3]
    assert tojson._fromdict({"name": "Alice", "age": 20}) == {"name": "Alice", "age": 20}
    assert tojson._frombytes("Alice".encode()) == "Alice"
    assert tojson._frombytes(bytes([97])) == "a"
    assert tojson._frombytearray(bytearray([97, 98, 99, 100, 101])) == "abcde"


    class User:
        def __init__(self, name: str, age: int) -> None:
            self.name = name
            self.age = age

    assert tojson._fromclass(User("Alice", 20)) == {"name": "Alice", "age": 20}
    assert tojson(User("Alice", 20)) == {"name": "Alice", "age": 20}
    # tojson._fromint = lambda x: x*2
    assert tojson().get(int)(123) == 123

    # tojson()
    with open("sample.json", "w", encoding="UTF-8") as f:
        json.dump(tojson([
            {
                "User1": User("Alice", 20),
                "User2": User("Bob", 24)},
            {"Enemy1": User("Slime", 300)}
        ], "data"), f, indent=4)
