def rotate_word(word, n):
    rotated_word = ''
    for letter in word:
        if ord(letter) >= ord('A') and ord(letter) <= ord('Z'):
            start = ord('A')
            rotated_word += chr(((ord(letter) - start) + n) % 26 + start)
        elif ord(letter) >= ord('a') and ord(letter) <= ord('z'):
            start = ord('a')
            rotated_word += chr(((ord(letter) - start) + n) % 26 + start)
    return rotated_word
    

print(rotate_word('cheer', 7))
print(rotate_word('melon', -10))