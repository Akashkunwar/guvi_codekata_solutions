# QID: 362
# 
# Given a string, find the length of the longest substring without repeating characters.
# Input Size : |S|<=1000
# Example:
# INPUT
# abcabcccdd
# OUTPUT
# 3
# 
# 
# 
# 


# Solution:


def longestUniqueSubsttr(string):
	last_idx = {}
	max_len = 0
	start_idx = 0
	for i in range(0, len(string)):
		if string[i] in last_idx:
			start_idx = max(start_idx, last_idx[string[i]] + 1)
		max_len = max(max_len, i-start_idx + 1)
		last_idx[string[i]] = i
	return max_len
string = str(input())
length = longestUniqueSubsttr(string)
print(str(length))
