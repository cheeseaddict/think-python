def do_n(f, n):
    if n <= 0:
        return
    f()
    do_n(f, n - 1)


def print_herro():
    print("Herro")


do_n(print_herro, 6)
