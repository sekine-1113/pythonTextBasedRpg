from ctypes import (
    byref,
    windll,
    wintypes,
)


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
        STD_OUTPUT_HANDLE = -11
        ENABLE_VIRTUAL_TERMINAL_PROCESSING = 0x0004

        kernel32 = windll.kernel32
        hOut = kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
        dwMode = wintypes.DWORD()
        kernel32.GetConsoleMode(hOut, byref(dwMode))
        dwMode.value |= ENABLE_VIRTUAL_TERMINAL_PROCESSING
        kernel32.SetConsoleMode(hOut, dwMode)