import itertools


class Key(int):
    pass


def keyGen() -> Key:
    s = "01010111"
    return Key(s, 2)


def Enc(m: str, key: Key) -> None:
    return int(m) ^ key


def Dec(c: str, key: Key) -> None:
    return Enc(c, key)

string = "Hello"
encrypted = ""
decrypted = ""

print(f"{string=}")

key = keyGen()
for s in string:
    a = ord(s)
    e = Enc(a, key)
    encrypted += chr(e)

for s in encrypted:
    d = Dec(ord(s), key)
    decrypted += chr(d)

print(f"{encrypted=}")
print(f"{decrypted=}")

print(f"{string==decrypted=}")