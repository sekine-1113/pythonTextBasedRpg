import os
import random
import sys
from copy import deepcopy


class Singleton:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance: Singleton = super(Singleton, cls).__new__(cls)
        return cls.__instance

    def get_instance(self):
        return self.__instance


def no_random(*args) -> int:
    return 0
