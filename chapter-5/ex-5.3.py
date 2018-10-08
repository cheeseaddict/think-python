def check_fermat(a, b, c, n):
    if a**n + b**n == c**n and n > 2:
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No that does not work")


def input_test_values():
    a = int(input("Enter a value for a: "))
    b = int(input("Enter a value for b: "))
    c = int(input("Enter a value for c: "))
    n = int(input("Enter a value for n: "))
    check_fermat(a, b, c, n)


input_test_values()
