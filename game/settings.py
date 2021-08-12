"""

"""

from hashlib import sha256
from getpass import getpass
import random
import string
import secrets


def make_ntoken(n: int=4):
    """make n bits token.

    args:
        (int) n: default = 4
    returns:
        (str) n bits token string.
    """
    alphabet = string.ascii_letters + string.digits
    password = "".join(secrets.choice(alphabet) for _ in range(n))
    print(password)
    return password


user = {
    "name": "Bob",
    "id": "",
    "password": ""
}


def make_id():
    k1 = "".join(random.choices(string.ascii_uppercase, k=2))
    k2 = "".join(random.choices(string.digits, k=4))
    user_id = k1 + k2
    return user_id


def make_password():
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
    user_id = make_id()
    print("ID:", user_id)
    user["id"] = user_id
    user_pass = make_password()
    user["password"] = user_pass

    if authrizer(user, user_id, user_pass):
        print("Login!")
    else:
        print("Invalid")


make_ntoken(16)