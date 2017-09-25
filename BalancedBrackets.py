
import sys

def isBalanced(s):
	pairs = { ')':'(',']':'[','}':'{','(':')','[':']',"{":"}" }
	stack = []
	for i in s:
		if len(stack)==0:
			stack.append(i)
			
		if i in "([{":
			stack.append(i)
		else:
			if stack[len(stack)-1] == pairs[i]:
				stack.pop()
			else:
				stack.append(i)

	if len(stack) ==0 : return 'YES'
	else : return 'NO' 

if __name__ == "__main__":
	t = int(input().strip())
	for a0 in range(t):
		s = input().strip()
		result = isBalanced(s)
		print(result)