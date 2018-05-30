#!/bin/python3

import sys

def primes(n):
	composite = [0 for i in range(n)]  # 1200th prime is 9733
	for i in range(2, 100):
		if not composite[i]:
			n = i * 2
			while n < n:
				composite[n] = 1
				n += i
	return [i for i in range(2, n) if not composite[i]]



def getPiles(stack,q):
	myPrimes = primes(10000)
	A = []
	B = []
	# iterations
	for i in range(q):
		while len(stack) != 0:
			tmp = stack.pop()
			if tmp % myPrimes[i] == 0:
				A.append(tmp)
			else:
				B.append(tmp)
		stack = A

	for a in A[::-1]:
		print (a)
	for b in B[::-1]:
		print (b)





def main():
	n, q = input().strip().split(' ')
	n, q = [int(n), int(q)]
	number = list(map(int, input().strip().split(' ')))
	stack = []
	for i in range(n):
		stack.append(number[i])

	getPiles(stack,q)




if __name__ == "__main__":
	main()

