# def runningMean(inputArr):
# 	inputArr.sort()
# 	if len(inputArr) == 0:
# 		return 0

# 	if len(inputArr)%2 == 1:
# 		return inputArr[int(len(inputArr)/2)]

# 	if len(inputArr)%2 == 0:
# 		idx1 = int( len(inputArr)/2)
# 		idx2 = int((len(inputArr)-1)/2)
# 		return float(inputArr[idx1]+inputArr[idx2])/2



# if __name__ == "__main__":
# 	n = int(input())
# 	inputArr = []
# 	for i in range(n):
# 		inp = int(input())
# 		inputArr.append(inp)
# 		print (runningMean(inputArr))