# https://www.hackerrank.com/challenges/sparse-arrays/problem

from collections import defaultdict

def main():
	freqDict = defaultdict(int)
	n = int(input().strip())
	for i in range(n):
		freqDict[ input().strip() ] +=1

	n = int(input().strip())
	for i in range(n):
		print ( freqDict[input().strip()] )



if __name__ == '__main__':
	main()