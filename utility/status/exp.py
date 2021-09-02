



class Exp:
    LIMIT_LEVEL = 100

    def __init__(self, current_exp, max_exp, min_exp) -> None:
        self.current_exp = current_exp
        self.max_exp = max_exp
        self.min_exp = min_exp

    def next_level_exp(self, curr_level):
        if curr_level >= self.LIMIT_LEVEL:
            return 0
        return ((curr_level-1)**2+125)*curr_level

    def diff_next_level_exp(self):
        return self.next_level_exp(self.calc_level())-self.current_exp

    def calc_level(self):
        for lv in range(1, self.LIMIT_LEVEL+1):
            if self.next_level_exp(lv) > self.current_exp:
                return lv
        return self.LIMIT_LEVEL

    def gain_exp(self, exp):
        old_level = self.calc_level()
        self.current_exp += exp
        if self.current_exp > self.max_exp:
            self.current_exp = self.max_exp
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