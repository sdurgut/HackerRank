def sumSquareDigits(n):
	i = 0
	num = n
	sum = 0
	while(num>0):
		digit = num%10
		num = (num-digit)/10
		sum += digit**2
	return sum

def main():
	maxNum = 1000000
	count = 0
	for i in range(maxNum+1):
		result = sumSquareDigits(i)
		if result ==1 or result == 89:
			count += 1
		else:
			while (result != 1 or result != 89):
				result = sumSquareDigits(result)
			

