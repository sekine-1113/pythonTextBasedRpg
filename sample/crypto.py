import secrets


class Key(int):
    pass


def keyGen(k: int=8) -> Key:
    s = str(bin(secrets.randbits(k)))
    return Key(s, 2)


def crypt(key, plain):
    def enc(m: str, key: Key) -> int:
        return int(m) ^ key
    encrypted = ""
    for s in plain:
        a = ord(s)
        e = enc(a, key)
        encrypted += chr(e)
    return encrypted

def decrypt(key, crypt):
    def dec(m: str, key: Key) -> int:
        return int(m) ^ key
    decrypted = ""
    for s in crypt:
        d = dec(ord(s), key)
        decrypted += chr(d)
    return decrypted


if __name__ == "__main__":
    k = keyGen()
    txt = "hello"
    print(txt)
    txt_ = crypt(k, txt)
    print(txt_)
    print(decrypt(k, txt_))