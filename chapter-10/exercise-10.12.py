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


def reverse_pairs(word_list):
	reversed_pair = []
	for word in word_list:
		reversed_word = word[::-1]
		if bisect(word_list, reversed_word):
			reversed_pair.append(word)

	return reversed_pair


words_txt_list = read_file()
print(reverse_pairs(words_txt_list))