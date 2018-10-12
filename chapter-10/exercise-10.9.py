def remove_duplicates(t):
    res = []
    
    if len(t) == 0: 
        return res

    for i in t:
        if i not in res:
            res.append(i)

    return res


print(remove_duplicates([1,2,1,1,1,222,3]))
print(remove_duplicates([1,1,1]))
print(remove_duplicates([]))