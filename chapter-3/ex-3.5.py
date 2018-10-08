# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +


def do_twice(f):
    f()
    f()


def do_four(f):
    do_twice(f)
    do_twice(f)


def vertical():
    print("+ - - - -", end="")


def horizontal():
    print("|        ", end="")


def row():
    do_twice(vertical)
    print("+")


def grid():
    do_twice(horizontal)
    print("|")


def print_row():
    row()
    do_four(grid)


def print_grid():
    do_twice(print_row)


def main():
    print_grid()
    row()


main()
