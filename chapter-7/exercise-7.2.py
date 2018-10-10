def square_root(a):
    x = 1
    epsilon = 0.0000001

    while True:
        y = (x + a/x) / 2
        if abs(y - x) < epsilon:
            break
        x = y

    return x

print(square_root(4))
