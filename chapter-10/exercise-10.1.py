def nested_sum(t):
    total = 0
    for num in t:
        if type(num) == list:
            total += nested_sum(num)
        else:
            total += num
    return total


print(nested_sum([1,[2, [3]]]))