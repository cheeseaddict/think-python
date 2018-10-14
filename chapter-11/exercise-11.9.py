def has_duplicates(t):
#    copy_t = t[:]
#    copy_t.sort()
    
#    for i in range(len(copy_t) - 1):
#        if copy_t[i] == copy_t[i + 1]:
#            return True 

#	Why did i not know about sets before?!?!
    return len(set(t)) < len(t)


def has_duplicates_2(t):
	d = {}

	for i in t:
		if i in d:
			return True
		else:
			d[i] = i
	return False

t = [1, 2, 3]
print(has_duplicates_2(t))
t.append(1)
print(has_duplicates_2(t))


t = [1, 2, 3]
print(has_duplicates(t))
t.append(1)
print(has_duplicates(t))5