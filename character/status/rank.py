
LIMIT_RANK = 20


class Rank:

    def __init__(self, current, max, min) -> None:
        self.current = current
        self.max = max
        self.min = min

    def next_rank_exp(self, curr_rank):
        if curr_rank >= LIMIT_RANK:
            return 0
        return ((curr_rank-1)**2+125)*curr_rank

    def diff_next_rank_exp(self):
        return self.next_rank_exp(self.calc_rank())-self.current

    def calc_rank(self):
        for rank in range(1, LIMIT_RANK+1):
            if self.next_rank_exp(rank) > self.current:
                return rank
        return LIMIT_RANK

    def gain_exp(self, exp):
        old_rank = self.calc_rank()
        self.current += exp
        if self.current > self.max:
            self.current = self.max
        new_rank = self.calc_rank()
        return new_rank-old_rank


if __name__ == "__main__":
    rank = Rank(0, 999999, 0)
    print(rank.calc_rank())
    rank.gain_exp(30000)
    print(rank.calc_rank())