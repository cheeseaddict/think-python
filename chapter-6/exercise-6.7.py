def is_power(a, b):
    if a < b:
        return False
    elif a == b:
        return True
    elif a % b == 0:
        return is_power(a/b, b)
    else:
        return False

print(is_power(8, 2))
print(is_power(15, 2))
