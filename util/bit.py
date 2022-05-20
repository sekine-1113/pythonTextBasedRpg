
class Status:
    NONE = 0x00
    POISON = 0x01
    MAHI = 0x02
    NEMURI = 0x04
    ALL = 0xFF

class Bit:
    def __init__(self, default_bit=None) -> None:
        self.bit = default_bit or 0x00

    def set_bit(self, new_bit):
        self.bit |= new_bit

    def get_bit(self):
        return self.bit

    def update_bit(self, new_bit):
        self.bit &= ~new_bit

    def has_bit(self, _bit):
        return ~self.bit & _bit

status_bit = Bit(Status.NONE)
status_bit.set_bit(Status.NEMURI)
print(status_bit.get_bit())
status_bit.update_bit(Status.NEMURI)
print(status_bit.get_bit())
print(status_bit.has_bit(Status.NEMURI))