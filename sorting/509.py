# QID: 509
# 
# Given an array of size N, find the minimum number of swaps required to sort the array.
# 
# Size of the array followed by the elements of the array
# 
# 
# Minimum number of swaps required
# 
# 
# Sample Input : 
# 4
# 4 3 2 1
# 
# Sample Output : 
# 2
# 


# Solution:


def minSwaps(arr):
	n = len(arr)
	arrpos = [*enumerate(arr)]
	arrpos.sort(key = lambda it : it[1])
	vis = {k : False for k in range(n)}
	ans = 0
	for i in range(n):
		if vis[i] or arrpos[i][0] == i:
			continue
		cycle_size = 0
		j = i
		while not vis[j]:
			vis[j] = True
			j = arrpos[j][0]
			cycle_size += 1
		if cycle_size > 0:
			ans += (cycle_size - 1)
	return ans
nn = input()
arr = [int(i) for i in input().split(" ")]
print(minSwaps(arr))