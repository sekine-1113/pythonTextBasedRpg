from pprint import pprint


def t_leven(s1, s2):
    if not s1: return len(s2)
    if not s2: return len(s1)
    if s1[0] == s2[0]: return t_leven(s1[1:], s2[1:])

    l1 = t_leven(s1, s2[1:])
    l2 = t_leven(s1[1:], s2)
    l3 = t_leven(s1[1:], s2[1:])
    return 1 + min(l1, l2, l3)
def t_lss(s1, s2):
    return (-t_leven(s1, s2)) / max(len(s1),len(s2)) + 1

# レーヴェンシュタイン距離
def lev(s, t):
    ls = len(s)
    lt = len(t)

    if not s: return lt
    if not t: return ls

    dp = [[0]*(lt+1)]*(ls+1)
    for j in range(1, lt+1):
        dp[0][j] = j

    for i in range(1, ls+1):
        dp[i][0] = i
        for j in range(1, lt+1):
            cost = not s[i-1] == t[j-1]
            dp[i][j] = min(
                dp[i-1][j] + 1,
                dp[i][j-1] + 1,
                dp[i-1][j-1] + cost)
    return dp[-1][-1]

def lss(s, t):
    m = max(len(s), len(t))
    v = lev(s, t)
    return 1 - (v / m)


# tst = [
#     ("ABC", ""),
#     ("", "ABC"),
#     ("ABC", "ABC"),
#     ("ABC", "BCD"),
#     ("ABC", "A")]
# for t in tst:
#     print(f"{t=} {t_lss(*t)=:.4} {lss(*t)=:.4}")

lev("かがわ", "かながわ")