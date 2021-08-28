class Key(int):
    pass


def keyGen() -> Key:
    return Key("01011111", 2)


def Enc(m: str, key: Key) -> None:
    return int(m) ^ key


def Dec(c: str, key: Key) -> None:
    return int(c) ^ key

string = "Hello"
encrypted = ""
decrypted = ""

print(f"{string=}")

for s in string:
    a = ord(s)
    e = Enc(a, keyGen())
    encrypted += chr(e)

for s in encrypted:
    d = Dec(ord(s), keyGen())
    decrypted += chr(d)

print(f"{encrypted=}")
print(f"{decrypted=}")

print(f"{string==decrypted=}")