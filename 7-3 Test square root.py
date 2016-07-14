import math

def sqrt(n):
    n = float(n)
    x = n / 2.0
    epsilon = 1e-15
    while True:
        y = (x + n/x) / 2
        if abs(y - x) < epsilon:
            return y
        x = y

for i in range(1, 10):
    i = float(i)
    print str(i) + " ", str(sqrt(i)) + " ", str(math.sqrt(i)) + " ", str(abs(sqrt(i) - math.sqrt(i))) + " "