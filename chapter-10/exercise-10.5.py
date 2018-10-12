def chop(t):
    del t[0]
    del t[-1]

    return


nums = [1,2,3,4,5]
print(chop(nums))
print(nums)


# Alternative, if we want to use slice (which creates a new list)
def chop_2(t):
    return t[1:-1]


nums_2 = [1,2,3,4,5]
rest = chop_2(nums_2)
print(rest)