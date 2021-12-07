
class Dictable:

    def asdict(self):
        r = {}
        for k, v in vars(self).items():
            if isinstance(v, Dictable):
                v = v.asdict()
            r[k] = v
        return r


class MyClass(object):
    def __init__(self) -> None:
        self._object = {}

    def bind(self, key, value):
        self.__setattr__(key, value)
        self.__setitem__(key, value)

    def __getitem__(self, key):
        return self._object.get(key)

    def __setitem__(self, key, value):
        self._object[key] = value
        self.__setattr__(key, value)
        return self

    def __getattr__(self, key):
        return self._object.get(key)

    def __setattr__(self, __name: str, __value) -> None:
        super().__setattr__(__name, __value)
        self._object.setdefault(__name, __value)


def TestMyClass():
    class Inner:
        def method(self): return "method"
    mycls = MyClass()
    mycls.bind("value", 10)
    assert mycls["value"] == mycls.value
    mycls.bind("add", lambda x,y: x+y)
    assert mycls["add"](3, 7) == mycls.add(4, 6)
    mycls["inner"] = Inner()
    assert mycls["inner"].method() == mycls.inner.method()
    mycls.method = Inner().method
    assert mycls["method"]() == mycls.method()
    print("OK")
    del mycls

if __name__ == "__main__":
    TestMyClass()