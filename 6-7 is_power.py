def is_power(a, b):
    a = float(a)
    b = float(b)
    if a**0.5 == b and a % b == 0 and (a/b)**0.5 == b:
        return True
    else:
        return False

print is_power(1, 1)