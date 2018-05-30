import math
from fractions import Fraction

def divisorGenerator(n):
	large_divisors = []
	for i in range(1, int(math.sqrt(n) + 1)):
		if n % i == 0:
			print("i",i)
			yield i
			if i*i != n:
				large_divisors.append(n / i)
	for divisor in reversed(large_divisors):
		print ("divisor",divisor)
		yield divisor

def is_square(integer):
	root = math.sqrt(integer)
	if int(root + 0.5) ** 2 == integer: 
		return True
	else:
		return False

def findEvenSquareDivisors(nums):
	for num in nums:
		divisors = list(divisorGenerator(num))
		# print(divisors[:-1])
		nCands = 0
		for div in divisors[:-1]:
			if div%2==0 and is_square(div):
				nCands +=1
		frac = Fraction(nCands, len(divisors)-1)
		if nCands ==0:
			print (0)
			continue
		print("{}/{}".format(frac.numerator,frac.denominator))




def main():
	ntestCases = int(input().strip())
	nums = []
	for i in range(ntestCases):
		nums.append(int(input().strip()))

	findEvenSquareDivisors(nums)



if __name__ == "__main__":
	main()