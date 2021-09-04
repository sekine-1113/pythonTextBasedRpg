


class Rank:

    LIMIT_RANK = 20

    def __init__(self, current_point, max_point, min_point) -> None:
        self.current_point = current_point
        self.max_point = max_point
        self.min_point = min_point

    def next_rank_point(self, curr_rank):
        if curr_rank >= self.LIMIT_RANK:
            return 0
        return ((curr_rank-1)**2+100)*curr_rank

    def diff_next_rank_point(self):
        return self.next_rank_point(self.calc_rank())-self.current_point

    def calc_rank(self):
        for rank in range(1, self.LIMIT_RANK+1):
            if self.next_rank_point(rank) > self.current_point:
                return rank
        return self.LIMIT_RANK

    def gain_point(self, point):
        old_rank = self.calc_rank()
        self.current_point += point
        if self.current_point > self.max_point:
            self.current_point = self.max_point
        new_rank = self.calc_rank()
        return new_rank-old_rank


if __name__ == "__main__":
    rank = Rank(0, 999999, 0)
    print(rank.calc_rank())
    print(rank.current_point)
    rank.gain_point(30000)
    print(rank.current_point)
    print(rank.calc_rank())