"""

"""

from hashlib import sha256
from getpass import getpass
import random
import string


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


def make_pass():
    password = ""

    while len(password) < 4:
        password = getpass()
    user_password = sha256(password.encode())
    return user_password.hexdigest()


def authrize(database, user_id, user_hased_password):
    valid = True
    if database["id"] != user_id:
        valid = False
    if database["password"] != user_hased_password:
        valid = False
    return valid



user_id = make_id()
print("ID:", user_id)
user["id"] = user_id
user_pass = make_pass()
user["password"] = user_pass

if authrize(user, user_id, user_pass):
    print("Login!")
else:
    print("Invalid")