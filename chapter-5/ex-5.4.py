def is_triangle(a, b, c):
    if (a + b > c) and (a + c > b) and (b + c > a):
        print("Triangle")
    else:
        print("No triangle!")


is_triangle(5,3,4)
is_triangle(5,3,12)
