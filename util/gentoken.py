
import random
import secrets
import string

from getpass import getpass
from hashlib import sha256



def create_token(n: int=16):
    """make N bits token.

    args:
        (int) n: default = 16
    returns:
        (str) n bits token string.

        ex. "WdbIiZRF7uC3eSJj"
    """
    alnum = string.ascii_letters + string.digits
    token = "".join(secrets.choice(alnum) for _ in range(n))
    return token


def create_id():
    k1 = "".join(random.choices(string.ascii_uppercase, k=2))
    k2 = "".join(random.choices(string.digits, k=4))
    user_id = k1 + k2
    return user_id


def get_password(n: int=4):
    password = ""
    while len(password) < n:
        password = getpass()
    user_password = sha256(password.encode())
    return user_password.hexdigest()


def create_random_password(n: int=16):
    alnum = string.ascii_letters + string.digits
    password = "".join(secrets.choice(alnum) for _ in range(n))
    row_password = password
    password = sha256(password.encode())
    return row_password, password.hexdigest()


def confirm_password(hashed_pass):
    password = getpass("Confirm Password:")
    user_password = sha256(password.encode())
    return user_password.hexdigest() == hashed_pass



def main():
    hpwd = get_password()
    print(confirm_password(hpwd))


if __name__ == "__main__":
    main()

