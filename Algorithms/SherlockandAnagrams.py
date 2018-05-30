from collections import Counter

def sort_string(word):
	return ''.join(sorted(word))

def count_anagrams(word):
	l = len(word)
	substrings = [sort_string(word[i:i+n]) for n in range(1, l) for i in range(0, l-n+1)]
	counter = Counter(substrings)
	sum_pairs = 0
	for v in counter.values():
		sum_pairs += v * (v-1) / 2
	return int(sum_pairs)

q = int(input().strip())
for a0 in range(q):
	s = input().strip()
	result = count_anagrams(s)
	print(result)
