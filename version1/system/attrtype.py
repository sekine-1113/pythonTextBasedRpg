none = 0
fire = 1
water = 2
wood = 3
t = ["none", "fire", "water", "wood"]

attr_type = [
    [1,   1,   1,   1],
    [1,   1, 0.5,   2],
    [1,   2,   1, 0.5],
    [1, 0.5,   2,   1]
]


for i in range(4):
    for j in range(4):
        print(f"{t[i]=} {t[j]=} {attr_type[i][j]=}")