from abc import ABCMeta

class Singleton(metaclass=ABCMeta):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance: Singleton = super(Singleton, cls).__new__(cls)
        return cls._instance
