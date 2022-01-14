from ctypes import byref, windll, wintypes
from datetime import datetime
from logging import DEBUG, ERROR, Handler, NullHandler, StreamHandler, getLogger, Formatter


class ColorStream:
    class Color:
        BLACK = "\033[30m"
        RED = "\033[31m"
        GREEN = "\033[32m"
        YELLO = "\033[33m"
        BLUE = "\033[34m"
        MAZENTA = "\033[35m"
        CIAN = "\033[36m"
        WHITE = "\033[37m"
        RESET = "\033[0m"
        N = "\033[38;5;{}m"

    class BackGroundColor:
        BLACK = "\033[40m"
        RED = "\033[41m"
        GREEN = "\033[42m"
        YELLO = "\033[43m"
        BLUE = "\033[44m"
        MAZENTA = "\033[45m"
        CIAN = "\033[46m"
        WHITE = "\033[47m"
        RESET = "\033[0m"
        N = "\033[48;5;{}m"

    def __init__(self) -> None:
        self.unlock()

    def unlock(self):
        # ANSIエスケープシーケンス解除
        STD_OUTPUT_HANDLE = -11
        ENABLE_VIRTUAL_TERMINAL_PROCESSING = 0x0004

        kernel32 = windll.kernel32
        hOut = kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
        dwMode = wintypes.DWORD()
        kernel32.GetConsoleMode(hOut, byref(dwMode))
        dwMode.value |= ENABLE_VIRTUAL_TERMINAL_PROCESSING
        kernel32.SetConsoleMode(hOut, dwMode)

    def red(self, message):
        return self.Color.RED + message + self.Color.RESET

    def normal(self, message):
        return message


class MyLogger:
    def __init__(self, _name, _logger_level=DEBUG, _handlers=None):
        self._name = _name
        self._logger = getLogger(_name)
        self._logger.setLevel(_logger_level)
        self._handlers = _handlers
        if self._handlers is not None:
            for handler, data in self._handlers.items():
                _level = data.get("level", _logger_level)
                _format = data.get("format", "[%(levelname)s] %(asctime)s %(filename)s %(message)s")
                _datefmt = data.get("datefmt", "%Y-%m-%d %H:%M:%S")
                self.addHandler(handler, _level, Formatter(fmt=_format, datefmt=_datefmt))

    def addHandler(self, handler, level, _formatter=None):
        if callable(handler):
            handler = handler()
        handler.setLevel(level)
        handler.setFormatter(_formatter)
        self._logger.addHandler(handler)

    def info(self):
        def wrapper(func):
            def inner(*args, **kwargs):
                self._logger.info(func.__name__)
                _object = func(*args, **kwargs)
                self._logger.info(func.__name__)
                return _object
            return inner
        return wrapper

    def getLogger(self):
        return self._logger


logger = MyLogger(__name__, DEBUG, {StreamHandler: {"level":DEBUG}})

@logger.info()
def func(*args):
    print("Hello")
    return 0

if __name__ == "__main__":
    func("mypy")