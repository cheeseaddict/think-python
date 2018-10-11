def print_backwards(s):
        i = len(s)

        while i > 0:
                letter = s[i - 1]
                print(letter)
                i -= 1

print_backwards('hello')
