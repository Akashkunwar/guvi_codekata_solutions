# QID: 60
# 
# Given an array, find the absolute minimum difference between any two elements in the array.
# Input Size : N <= 1000000(complexity O(n) or O(nlogn))
# 
# 
# Sample Testcase :
# INPUT
# 5
# 0 2 3 4 5
# OUTPUT
# 1
# 
# 
# 
# 


# Solution:


def findMinDiff(arr, n):
	diff = 10**20
	for i in range(n-1):
		for j in range(i+1,n):
			if abs(arr[i]-arr[j]) < diff:
				diff = abs(arr[i] - arr[j])
	return diff
aa = input()
arr = [int(i) for i in input().split(" ")]
n = len(arr)
print(str(findMinDiff(arr, n)))