prefixes = "JKLMNOPQ"
suffix = "ACK"

for letter in prefixes:
    if letter == "O" or letter == "Q":
        print(letter + 'U' + suffix)
    print(letter + suffix)