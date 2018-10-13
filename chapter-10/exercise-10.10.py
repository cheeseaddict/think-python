import time


def read_file():
    res = []
    with open('words.txt', 'r') as f:
        for lines in f:
            word = lines.strip()
            res.append(word)

    return res

# print(read_file())

def read_file_2():
    res = []
    with open('words.txt', 'r') as f:
        for lines in f:
            word = lines.strip()
            res = res + [word]

    return res


start = time.time()
read_file()
end = time.time()
first = end - start
print(first)

start_2 = time.time()
read_file_2()
end_2 = time.time()
second = end_2 - start_2
print(second)