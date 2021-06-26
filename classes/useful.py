

class Dictable:
    def asdict(self):
        r = {}
        for k, v in vars(self).items():
            if isinstance(v, Dictable): v = v.asdict()
            r[k] = v
        return r