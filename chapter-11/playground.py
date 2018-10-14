def histogram(s):
	d = dict()
	for c in s:
		if c not in d:
			d[c] = 1
		else:
			d[c] += 1
	return d


def print_hist(h):
	for c in h:
		print(c, h[c])


def reverse_lookup(d, v):
	for k in d:
		if d[k] == v:
			return k

	raise LookupError()


def invert_dict(d):
	inverse = dict()
	for key in d:
		val = d[key]
		if val not in inverse:
			inverse[val] = [key]
		else:
			inverse[val].append(key)
	return inverse


h = histogram("brontosaurus")
print(h)
inverse = invert_dict(h)
print(inverse)