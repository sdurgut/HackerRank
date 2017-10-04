import itertools
def generate(s):
	for i, j in itertools.combinations(range(len(s)+1), 2):
		yield s[i:j]


def minion_game(string):
	vovels = "AEIOU"
	stuartScore = 0
	kevinScore = 0
	combinations = list(generate(string))
	for substring in combinations:
		if substring[0] in vovels:
			kevinScore +=1
		else:
			stuartScore +=1
	if kevinScore>stuartScore:
		return "Kevin " + str(kevinScore)
	elif kevinScore<stuartScore:
		return "Stuart " + str(stuartScore)
	else:
		return "Draw"


if __name__ == '__main__':
	s = input()
	print (minion_game(s))


# def score_word(word):
#     stuart = 0
#     kevin = 0
#     for index, character in enumerate(word):
#         if character in "AEIOU":
#             kevin += len(word) - index
#         else:
#             stuart += len(word) - index
#     if stuart > kevin:
#         print ("Stuart " + str(stuart))
#     elif stuart < kevin:
#         print ("Kevin " + str(kevin))
#     else:
#         print ("Draw")

# if __name__ == "__main__":
#     print(score_word(sys.stdin.read().strip()))