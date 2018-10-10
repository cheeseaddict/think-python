import math


# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         recurse = factorial(n - 1)
#         result = n * recurse
#         return result


def estimate_pi():
    k = 0
    total = 0
    factor = 2*math.sqrt(2) / 9801

    while True:
        numerator = float((math.factorial(4*k)) * (1103 + 26390 * k))
        denominator = float((math.factorial(k)**4) * 396**(4*k))
        term = factor * (numerator / denominator)
        total = total + term

        if(abs(term) < 1e-15):
            break

        k = k + 1

    return 1 / total


print(estimate_pi())
