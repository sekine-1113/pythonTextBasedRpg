from games.cui.textbasedrpg.alpha.core import ABC, abstractmethod


class _Command(ABC):

    @abstractmethod
    def execute(self):
        pass