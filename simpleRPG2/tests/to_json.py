
import json


class Jsonable:
    def __init__(self, *args, **kwargs):
        pass

    def tojson(self):
        from copy import deepcopy
        d = deepcopy(self.__dict__)
        rem_keys = []
        for key, value in d.items():
            if key[0] == "_":
                rem_keys.append(key)
            if hasattr(value, "tojson"):
                d[key] = value.tojson()
        for key in rem_keys:
            del d[key]
        return json.loads(json.dumps(d, indent=4))


def tojson(_class):
    if hasattr(_class, "tojson"):
        return _class.tojson()

    from copy import copy

    d = copy(_class.__dict__)
    rem_keys = []
    key: str
    for key, value in d.items():
        if key.startswith("_"):
            rem_keys.append(key)
        if value.__class__ not in [bool,int,float,str,list,tuple,dict]:
            d[key] = tojson(value)
    for key in rem_keys:
        del d[key]
    return json.loads(json.dumps(d, indent=4))


class MyClass(Jsonable):
    def __init__(self) -> None:
        self.name = "MyClass"



print(MyClass().tojson())
print(tojson(MyClass()))