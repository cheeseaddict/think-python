def count(word, le):
    count = 0
    for letter in word:
        if letter == le:
            count += 1
    return count

print(count('banana', 'a'))
print(count('hello', 'l'))