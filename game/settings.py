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
    print(user_id)
    return user_id


def make_pass():
    password = ""

    while len(password) < 4:
        password = getpass()
    user_password = sha256(password.encode()).hexdigest()
    print(user_password)
    return user_password


print("ID:")
make_id()
make_pass()