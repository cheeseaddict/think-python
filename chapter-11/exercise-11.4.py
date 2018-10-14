def histogram(s):
	d = dict()
	for c in s:
		if c not in d:
			d[c] = 1
		else:
			d[c] += 1
	return d


def reverse_lookup(d, v):
	res = []
	for k in d:
		if d[k] == v:
			res.append(k)
	return res
	

h = histogram("brontosaurus")
k = reverse_lookup(h, 2)
print(k)