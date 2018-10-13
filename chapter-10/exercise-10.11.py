def read_file():
    res = []
    with open('words.txt', 'r') as f:
        for lines in f:
            word = lines.strip()
            res.append(word)

    return res


def bisect(sorted_list, target):
	start = 0
	end = len(sorted_list) - 1

	while start <= end:
		middle = (start + end) // 2
		if sorted_list[middle] < target:
			start = middle + 1
		elif sorted_list[middle] > target:
			end = middle - 1
		else:
			return middle

	return None



words_txt_list = read_file()
print(bisect(words_txt_list, 'ovular'))
print(bisect([1,2,3,4,5], 1))