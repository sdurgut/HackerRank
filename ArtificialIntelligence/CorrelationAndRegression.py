# https://www.hackerrank.com/challenges/correlation-and-regression-lines-6/problem
import math
def main():
	p = [15,12,8,8,7,7,7,6,5,3]
	h = [10,25,17,11,13,17,20,13,9,15]
	p2 = []
	h2 = []
	ph = []
	for i in range(len(p)):
		p2.append(p[i]**2)
		h2.append(h[i]**2)
		ph.append(p[i]*h[i])

	# pearson correlation coefficient
	correlation  = (len(p)*sum(ph)-sum(p)*sum(h))/math.sqrt( (len(p)*sum(p2)-sum(p)**2)*(len(p)*sum(h2)-sum(h)**2) )

	print (correlation)



if __name__ == '__main__':
	main()