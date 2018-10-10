import math


def test_square_root():
    for i in range(1, 10):
        square_root_lib = math.sqrt(i)
        square_root_function = square_root(i)
        diff = abs(square_root_function - square_root_lib)

        print('{0:.2f} {1: .12f} {2: .12f} {3: .12e}'.format(i, square_root_function, square_root_lib, diff))


def square_root(a):
    x = 1
    epsilon = 0.0000001

    while True:
        y = (x + a/x) / 2
        if abs(y - x) < epsilon:
            break
        x = y

    return x


test_square_root()
