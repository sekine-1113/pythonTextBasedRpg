
import random
import secrets
import string

from getpass import getpass
from hashlib import sha256


def create_ntoken(n: int=16):
    """make N bits token.

    args:
        (int) n: default = 16
    returns:
        (str) n bits token string.

        ex. "WdbIiZRF7uC3eSJj"
    """
    alnum = string.ascii_letters + string.digits
    token = "".join(secrets.choice(alnum) for _ in range(n))
    del alnum
    return token


def create_id():
    k1 = "".join(random.choices(string.ascii_uppercase, k=2))
    k2 = "".join(random.choices(string.digits, k=4))
    user_id = k1 + k2
    del k1, k2
    return user_id


def create_password(n: int=4):
    password = ""
    while len(password) < n:
        password = getpass()
    user_password = sha256(password.encode())
    del password
    return user_password.hexdigest()


def confirm_password():
    password = getpass("Confirm Password:")
    user_password = sha256(password.encode())
    del password
    return user_password.hexdigest()


def authrizer(database, user_id, user_hased_password):
    valid = True
    if database["id"] != user_id:
        valid = False
    if database["password"] != user_hased_password:
        valid = False
    return valid


def main():
    create_ntoken()
    user = {
        "name": "Bob",
        "id": "",
        "password": ""
    }
    user_id = create_id()
    print("ID:", user_id)
    user["id"] = user_id
    user_pass = create_password()
    user["password"] = user_pass
    user_pass = confirm_password()
    if authrizer(user, user_id, user_pass):
        print("Login!")
    else:
        print("Invalid")


main()
