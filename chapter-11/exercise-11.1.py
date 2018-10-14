def read_file():
    index = 0
    res = {}

    with open('words.txt', 'r') as f:
    	
        for lines in f:
            word = lines.strip()
            res[word] = index
            index += 1

    return res


def check_dic(s):
	build_dic = read_file()

	if s in build_dic:
		return True

print(read_file())
print(check_dic("zooid"))
print(check_dic("herro"))