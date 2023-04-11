class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except C:
        print("C")
    except D:
        print("D")
    except B:
        print("B")
