
LIMIT_LEVEL = 100


class Exp:

    def __init__(self, current, max, min) -> None:
        self.current = current
        self.max = max
        self.min = min

    def next_level_exp(self, curr_level):
        if curr_level >= LIMIT_LEVEL:
            return 0
        return ((curr_level-1)**2+125)*curr_level

    def diff_next_level_exp(self):
        return self.next_level_exp(self.calc_level())-self.current

    def calc_level(self):
        for lv in range(1, LIMIT_LEVEL+1):
            if self.next_level_exp(lv) > self.current:
                return lv
        return LIMIT_LEVEL

    def gain_exp(self, exp):
        old_level = self.calc_level()
        self.current += exp
        if self.current > self.max:
            self.current = self.max
        new_level = self.calc_level()
        return new_level-old_level


if __name__ == "__main__":
    exp = Exp(0, 9999999, 0)
    print(exp.calc_level())
    exp.gain_exp(10000)
    print(exp.calc_level())
    print(exp.diff_next_level_exp())
    exp.gain_exp(1024)
    print(exp.calc_level())
    exp.gain_exp(1)
    print(exp.calc_level())