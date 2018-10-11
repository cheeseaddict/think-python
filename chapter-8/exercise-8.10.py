def is_palindrome(word):
    return word == word[::-1]

print(is_palindrome('herro'))
print(is_palindrome('rotor'))
print(is_palindrome('r'))
print(is_palindrome('civic'))