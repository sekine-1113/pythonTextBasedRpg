"""

"""

from hashlib import sha256
from getpass import getpass
import random
import string
import secrets


def create_ntoken(n: int=16):
    """make N bits token.

    args:
        (int) n: default = 16
    returns:
        (str) n bits token string.

        ex. "WdbIiZRF7uC3eSJj"
    """
    alphabet = string.ascii_letters + string.digits
    token = "".join(secrets.choice(alphabet) for _ in range(n))
    print(token)
    return token


user = {
    "name": "Bob",
    "id": "",
    "password": ""
}


def create_id():
    k1 = "".join(random.choices(string.ascii_uppercase, k=2))
    k2 = "".join(random.choices(string.digits, k=4))
    user_id = k1 + k2
    return user_id


def create_password():
    password = ""
    while len(password) < 4:
        password = getpass()
    user_password = sha256(password.encode())
    return user_password.hexdigest()


def authrizer(database, user_id, user_hased_password):
    valid = True
    if database["id"] != user_id:
        valid = False
    if database["password"] != user_hased_password:
        valid = False
    return valid


def main():
    user_id = create_id()
    print("ID:", user_id)
    user["id"] = user_id
    user_pass = create_password()
    user["password"] = user_pass

    if authrizer(user, user_id, user_pass):
        print("Login!")
    else:
        print("Invalid")


create_ntoken(16)