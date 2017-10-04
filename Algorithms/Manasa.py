import itertools

def manasa(numbers):
	res = []
	for number in numbers:
		isDiv = False
		for c in itertools.permutations(number, min(len(number), 3)):
			if int(''.join(c)) % 8 == 0:
				isDiv = True
				res.append("YES")
		if isDiv==False:
			res.append("NO")
	return res



if __name__ == '__main__':
	N = int(input().strip())
	numbers = []
	for i in range(N):
		numbers.append( input().strip() )
	res = manasa(numbers)
	for i in res:
		print (i)

