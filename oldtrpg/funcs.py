def int_input(txt):
    while True:
        try: return int(input(txt+">> "))
        except ValueError: continue

def call(d_count=0,txt="",min_count=0):
    while True:
        inp = int_input(txt)
        if min_count <= inp <= d_count-1:
            return inp