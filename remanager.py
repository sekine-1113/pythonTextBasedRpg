import os


class ResourceManager:
    def __init__(self, abs_path=False) -> None:
        self.__resources = {}
        self._abs_path = abs_path

    def add(self, key, value):
        self.__resources.setdefault(key, value)

    def get(self, key):
        path = self.__resources.get(key)
        if self._abs_path:
            path = os.path.abspath(path)
        return path

    def show(self):
        return self.__resources


resource = ResourceManager(True)
resource.add("backup", "./backup")
print(resource.get("backup"))