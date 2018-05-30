def fib(n):
	a,b = 0,1
	for _ in range(n):
		a,b = b,a+b
	return a


def fibR(n):
	if n==0:
		print("AAAAAAAAAAAAAAAA")
		return 0
	elif n==1:
		return 1
	else:
		return fibR(n-1) + fibR(n-2)

# for i in range(100):
# 	print(fib(i))
print("######################")
for i in range(10):
	print(fibR(i))