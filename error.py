
class TexeBasedRPGError(Exception):
    def __init__(self, message, code=None, params=None):
        self.message = message
        self.code = code
        self.params = params

def main():
    a = 0
    try:
        if a:
            raise TexeBasedRPGError("a is true! Error", 123)
        else:
            raise TexeBasedRPGError("raise Error", 234)
    except TexeBasedRPGError as e:
        print(f"[{e.code}] {e.message}")

main()