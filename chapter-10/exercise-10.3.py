def cumsum(t):
    res = []
    total = 0
    for i in range(len(t)):
        total += t[i]
        res.append(total)

    return res



print(cumsum([1,2,3]))
print(cumsum([1,2,3,4]))