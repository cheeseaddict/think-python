import random


def has_duplicates(t):
    copy_t = t[:]
    copy_t.sort()
    
    for i in range(len(copy_t) - 1):
        if copy_t[i] == copy_t[i + 1]:
            return True 

    return False


def random_students():
    t = []

    for i in range(23):
        t.append(random.randint(1, 365))

    return t


def matches(runs):
    count = 0
    for i in range(runs):
        if has_duplicates(random_students()):
            count += 1
    return count / runs

runs = 365
print(matches(runs))