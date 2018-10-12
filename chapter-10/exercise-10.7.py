def is_anagram(word1, word2):
    word1 = ''.join(word1.split())
    word2 = ''.join(word2.split())

    if len(word1) != len(word2):
        return False

    for letter in word1:
        if letter not in word2:
            return False

    return True


print(is_anagram("restful", "fluster"))
print(is_anagram("adultery", "true lady"))
print(is_anagram("adultery", "true lady asdadsasd"))
print(is_anagram("ahashsah", "hellO"))