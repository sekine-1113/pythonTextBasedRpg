import os
import random
import sys

from abc import (
    ABC,
    abstractmethod,
)
from copy import (
    copy,
    deepcopy
)


def integer(prompt:str="> ") -> int:
    user_input = input(prompt)
    try:
        user_input = int(user_input)
        return user_input
    except ValueError as e:
        return integer(prompt)