def GCD(a, b):
    if b == 0:
        print a
        return
    r = a % b
    GCD(b, r)

GCD(-2, -4)
