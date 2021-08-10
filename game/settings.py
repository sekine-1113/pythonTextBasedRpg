"""

"""

from hashlib import sha256
from getpass import getpass


user = {
    "name": "Bob",
    "password": ""
}

password = ""

while len(password) < 4:
    password = getpass()
    print(password)
    a = sha256(password.encode()).hexdigest()
    print(a)

user["password"] = a
print(user["password"])


