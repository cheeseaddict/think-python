import math


def eval_loop():
    while True:
        user_cmd = input('> ')
        if user_cmd == 'done':
            break

        print(eval(user_cmd))


eval_loop()
