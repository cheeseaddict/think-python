# Exercise 3.1. Move the last line of this program to the top,
# so the function call appears before the definitions.
# Run the program and see what error message you get.

# Exercise 3.2.
# Move the function call back to the bottom and move the definition of print_lyrics
# after the definition of repeat_lyrics. What happens when you run this program?


def repeat_lyrics():
    print_lyrics()
    print_lyrics()


def print_lyrics():
    print("I'm a lumberjack, and I'm okay")
    print("I sleep all night and I work all day.")


repeat_lyrics()


def print_twice(bruce):
    print(bruce)
    print(bruce)


def cat_twice(part1, part2):
    cat = part1 + part2
    print_twice(cat)


line1 = "Bing tiddle "
line2 = "tiddle bang."

cat_twice(line1, line2)
