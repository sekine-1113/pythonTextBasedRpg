import os


class ResourceManager:
    def __init__(self, abs_path=False, sub=False) -> None:
        self.__resources = {}
        self._abs_path = abs_path
        self._sub = sub

    def add(self, key, value):
        self.__resources.setdefault(key, value)

    def get(self, key=None):
        if key is None:
            return self.__resources
        path: str = self.__resources.get(key)
        if self._sub:
            if "{" in path and "}" in path:
                s=path.find("{")
                e=path.find("}")
                old=path[s:e+1]
                new_=old.removeprefix("{").removesuffix("}")
                t=self.get(new_)
                path = path.replace(old,t)
                if "/" in path:
                    paths = path.split("/")
                else:
                    paths = path.split("\\")
                path = os.path.join("", *paths)
        if self._abs_path:
            path = os.path.abspath(path)
        return path

    def show(self):
        return self.__resources


resource = ResourceManager(True)
resource.add("current", "./")
resource.add("backup", "{current}/backup")
resource.add("assets", "{current}/assets")
print(resource.get("backup"))