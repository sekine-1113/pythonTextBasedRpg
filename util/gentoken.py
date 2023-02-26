
import random
import secrets
import string
from getpass import getpass
from hashlib import sha256


def create_token(n: int=16) -> str:
    """create N bits token.

    args:
        (int) n: default = 16
    returns:
        (str) n bits token string.

        ex. "WdbIiZRF7uC3eSJj"
    """
    alnum = string.ascii_letters + string.digits
    token = "".join(secrets.choice(alnum) for _ in range(n))
    return token


def create_id(uasc_k: int=2, dig_k: int=4, format="") -> str:
    """create id.

    args:
        (int) uasc_k: default = 2
        (int) dig_k: default = 4
    returns:
        (str) (uasc_k + dig_k) bits id string.

        ex. "AB1234"
    """
    k1 = "".join(random.choices(string.ascii_uppercase, k=uasc_k))
    k2 = "".join(random.choices(string.digits, k=dig_k))
    user_id = k1 + k2
    if format != "":
        user_id = format.format(k1, k2)
    return user_id


def get_password(n: int=4) -> str:
    """ユーザーからnビット以上のパスワードの入力を求める"""
    password = ""
    while len(password) < n:
        password = getpass()
    user_password = sha256(password.encode())
    return user_password.hexdigest()


def create_random_password(n: int=16) -> tuple[str]:
    """nビット以上のランダムなパスワードを作成する"""
    alnum = string.ascii_letters + string.digits
    password = "".join(secrets.choice(alnum) for _ in range(n))
    row_password = password
    password = sha256(password.encode())
    return row_password, password.hexdigest()


def confirm_password(hashed_pass: str) -> bool:
    """ハッシュ化されたパスワードを引数とし、パスワードを入力して一致するかどうかを返す"""
    password = getpass("Confirm Password:")
    user_password = sha256(password.encode())
    return user_password.hexdigest() == hashed_pass


def hased(plain: str) -> str:
    """プレーンテキストをハッシュ化する"""
    if isinstance(plain, bytes|bytearray):
        return sha256(plain).hexdigest()
    return sha256(plain.encode()).hexdigest()


def main():
    hpwd = get_password()
    print(confirm_password(hpwd))


if __name__ == "__main__":
    # main()
    print(create_id(0, 6))


