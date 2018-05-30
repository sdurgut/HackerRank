#!/bin/python3
# https://www.hackerrank.com/challenges/grading/problem

import sys

def solve(grades):
	res = []
	for g in grades:
		if g < 38:
			res.append(g)
		elif g%5>2:
				res.append(g+(5-g%5) )
		else:
			res.append(g)
	return res





n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))
