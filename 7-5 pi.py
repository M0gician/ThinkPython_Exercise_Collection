# import math
#
# def estimate_pi():
#     constant = (2 * 2**0.5) / (9801)
#     k = 0
#     result = 0
#
#     while k >= 0:
#         num = (math.factorial(4 * k)) * (1103 + 26390 * k)
#         den = (math.factorial(k)**4) * (396**(4 * k))
#         term = num / den
#         epsilon = 1e-15
#
#         if term >= epsilon:
#             k += 1
#             result = result + term
#         else:
#             esti_pi = 1 / (constant * result)
#             error = abs(math.pi - esti_pi)
#             print esti_pi
#             print error
#             return esti_pi
#
#
# estimate_pi()

import math


def factorial(n):
    """Computes factorial of n."""
    if n == 0:
        return 1
    else:
        recurse = factorial(n - 1)
        result = n * recurse
        return result



def estimate_pi():
    """Computes an estimate of pi.

    Algorithm due to Srinivasa Ramanujan, from
    http://en.wikipedia.org/wiki/Pi
    """
    total = 0
    k = 0
    factor = 2 * math.sqrt(2) / 9801
    while True:
        num = factorial(4 * k) * (1103 + 26390 * k)
        den = factorial(k) ** 4 * 396 ** (4 * k)
        term = factor * num / den
        total += term

        if abs(term) < 1e-15: break
        k += 1

    return 1 / total

print estimate_pi()