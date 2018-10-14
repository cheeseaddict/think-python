def histogram(s):
	d = dict()
	for c in s:
		if c not in d:
			d[c] = 1
		else:
			d[c] += 1
	return d


def invert_dict(d):
	inverse = dict()
	for key, value in d.items():
		group = inverse.setdefault(value, [])
		group.append(key)
	return inverse


h = histogram("brontosaurus")
print(h)
inverse = invert_dict(h)
print(inverse)