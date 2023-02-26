from ctypes import byref, windll, wintypes


class Fore:
    RED = ""
    RESET = ""


def init():
    STD_OUTPUT_HANDLE = -11
    ENABLE_VIRTUAL_TERMINAL_PROCESSING = 0x0004

    kernel32 = windll.kernel32
    hOut = kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    dwMode = wintypes.DWORD()
    kernel32.GetConsoleMode(hOut, byref(dwMode))
    dwMode.value |= ENABLE_VIRTUAL_TERMINAL_PROCESSING
    kernel32.SetConsoleMode(hOut, dwMode)



if __name__ == "__main__":
    init()