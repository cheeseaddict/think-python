def histogram(s):
	d = dict()
	for c in s:
		if c not in d:
			d[c] = 1
		else:
			d[c] += 1
	return d


def print_hist(h):
	for key in sorted(h):
		print(key, h[key])


h = histogram("brontosaurus")
print_hist(h)