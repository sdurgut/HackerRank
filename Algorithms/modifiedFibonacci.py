def modFib(t1,t2,n):
	idx = 2
	tCur = t2
	tPrev = t1
	
	tmp = 0
	while idx < n:
		tmp = tPrev + tCur*tCur
		# print 'tPrev,tCur = ', tPrev, tCur
		tPrev = tCur
		tCur = tmp
		idx = idx + 1

	return tCur


s =raw_input().strip()
L = s.split()
print L
print modFib(int(L[0]), int(L[1]), int(L[2])) 


