

class ConstDict(dict):

    def __setitem__(self, __k, __v) -> None:
        if (__v:=self.__getitem__(__k)):
            return
        return super().__setitem__(__k, __v)


CONFIG = ConstDict({
    "CONST": "hogehoge"
})

CONFIG["CONST"] = "aaaa"

print(CONFIG["CONST"])