import os


class ResourceManager:
    def __init__(self, current_dirctory=__file__) -> None:
        if os.path.isfile(current_dirctory):
            current_dirctory = os.path.dirname(current_dirctory)
        self._curr_dir = current_dirctory

    def path(self):
        pass

    def current(self):
        return self._curr_dir


print(ResourceManager().current())