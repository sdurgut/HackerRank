def myf(T,N):
	canReach = False
	steps = 0
	for i in range(T+1):
		if N == (i+2)*(i+3)/2:
			steps = i
			canReach = True
			break

	if canReach:
		return "Go On Bob {}".format(steps+2)
	else:
		return "Better Luck Next Time"

if __name__ == "__main__":
	T = int(input().strip())
	for i in range(T):
		N = int(input().strip())
		print(myf(T,N))


# a= [12838444,12832170,16755752,17512152,14149490,9426651,10313467,72847783,48788839,39405721,84733499,52485318,
# 	41216910,36798270,52989691,89938402,32866639,94307968,85682734,31397766,26903323,49887349,30948778,37831951,
# 	15615911,23356002,97582,96213174,68928190,1691257,57288558,68821171,74731802,918690,2087946]	
# for i in a:
# 	print (myf(10000,i))