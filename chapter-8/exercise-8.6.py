def find(word, letter, start=0):
    index = start
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1


def count(word, letter):
    count = 0
    index = 0

    while True:
        index = find(word, letter, index)
        
        if index == -1:
            break

        count += 1
        index += 1

    return count


print(count('banana', 'a'))
print(count('hello', 'l'))