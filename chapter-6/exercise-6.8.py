def gcd(a, b):
    if a == b:
        return a
    elif a > b:
        return gcd(a-b, b)
    elif b > a:
        return gcd(a, b-a)


print(gcd(84, 132))
print(gcd(246, 642))
print(gcd(41, 107))
