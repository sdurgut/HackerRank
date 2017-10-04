def quicksort(arr, lo, hi):
	if lo < hi:
		p = partition(arr, lo, hi)
		quicksort(arr, lo, p)
		quicksort(arr, p + 1, hi)

def partition(arr, lo, hi):
	print (arr,lo,hi)
	pivot = arr[hi]
	i = lo    
	for j in range (i, hi):
		if arr[j] < arr[i]:
			i = i + 1
			arr = swap(arr,i,j)
	if arr[pivot] < arr[i]:
		arr = swap(arr,i + 1,hi)
	print (arr)
	return i + 1

def swap(arr,i,j):
	tmp = i
	arr[i] = arr[j]
	arr[j] = arr[tmp]
	return arr



# # Like Python indexing, lo to hi-1

# def quicksort(arr, lo=0, hi=-1):
#     if hi == -1:
#         hi = len(arr)
#     if lo < hi - 1:
#         p = partition(arr, lo, hi)
#         quicksort(arr, lo, p)
#         quicksort(arr, p + 1, hi)


# def partition(arr, lo, hi):
#     p_val = arr[hi-1]
#     j = lo
#     for i in xrange(lo, hi-1):
#         if arr[i] < p_val:
#             arr[i], arr[j] = arr[j], arr[i]
#             j += 1
#     arr[hi-1], arr[j] = arr[j], arr[hi-1]
#     print " ".join(map(str, arr))
#     return j




if __name__ == "__main__":
	n = int(input().strip())
	s = input().split()
	arr = [int(i) for i in s]
	quicksort(arr,0,len(arr)-1)
	print (arr)