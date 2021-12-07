import secrets


class Key(int):
    pass


def keyGen(k: int=8) -> Key:
    s = str(bin(secrets.randbits(k)))
    return Key(s, 2)


string = "Hello"

print(f"{string=}")

key = keyGen()

def crypt(key):
    def Enc(m: str, key: Key) -> int:
        return int(m) ^ key
    encrypted = ""
    for s in string:
        a = ord(s)
        e = Enc(a, key)
        encrypted += chr(e)
    return encrypted

def decrypt(key, encrypt):
    def Dec(m: str, key: Key) -> int:
        return int(m) ^ key
    decrypted = ""
    for s in encrypt:
        d = Dec(ord(s), key)
        decrypted += chr(d)
    return decrypted

crypted = crypt(key)
decrypted = decrypt(key, crypted)
print(f"{crypted=}\n{decrypted=}")

print(f"{string==decrypted=}")