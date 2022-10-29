
def levenshtein(s: str, t: str) -> int:
    s = s.lower()
    t = t.lower()

    ls = len(s)
    lt = len(t)
    if not s: return lt
    if not t: return ls

    dp = [ [0]*(lt+1) for _ in range(ls+1) ]
    for j in range(1, lt+1):
        dp[0][j] = j
    for i in range(1, ls+1):
        dp[i][0] = i
        for j in range(1, lt+1):
            cost = not s[i-1] == t[j-1]
            dp[i][j] = min(
                dp[i-1][j-1] + cost,
                dp[i-1][j] + 1,
                dp[i][j-1] + 1
            )
    return dp[-1][-1]


def normalize(s, t):
    return 1 - levenshtein(s, t) / max(len(s), len(t))


if __name__ == "__main__":
    t = 0.6

    allow_str = ["hello", "world", "good", "python","god"]
    while True:
        user_input = input(">> ")
        if user_input in allow_str:
            continue
        else:
            maybe = [(0, "")]
            for s in allow_str:
                n = normalize(user_input, s)
                if n >= t:
                    maybe.append((n, s))
            max_ = max([m[0] for m in maybe])
            maybe_word = list(filter(lambda x: x[0]==max_, maybe))[0][1]
            print(f"Could it be '{maybe_word}'?")



