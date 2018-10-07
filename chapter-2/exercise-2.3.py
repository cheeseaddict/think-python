import math


def sphere(r):
    return 4/3 * math.pi * r**3

print(sphere(5)) # 523.5987755982989


def book_price(amount):
    book_price = 24.95
    book_discount = 0.6
    shipping = 3
    additional_shipping = 0.75

    return (book_price * book_discount * amount) + shipping + additional_shipping*(amount-1)

print(book_price(60)) # 945.4499999999999