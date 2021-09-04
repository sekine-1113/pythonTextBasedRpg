import secrets


class Key(int):
    pass


def keyGen(k: int=8) -> Key:
    s = str(bin(secrets.randbits(k)))
    return Key(s, 2)


def Enc(m: str, key: Key) -> int:
    return int(m) ^ key


def Dec(c: str, key: Key) -> int:
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