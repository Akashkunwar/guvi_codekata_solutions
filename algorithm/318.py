# QID: 318
# 
#  Given a number N followed by N numbers. Keep the count of each number and print the maximum repeating number.
# Input Size : N <= 100000 
# 
# 
# Sample Testcase :
# INPUT
# 5
# 15 5 -20 -20 -45
# OUTPUT
# -20
# 
# 
# 
# 


# Solution:


def maxRepeating(arr, n, k):
	for i in range(0, n):
		arr[arr[i]%k] += k
	max = arr[0]
	result = 0
	for i in range(1, n):
	
		if arr[i] > max:
			max = arr[i]
			result = i
	return result
k = int(input())
arr = [int(i) for i in input().split(" ")]
n = len(arr)
print(maxRepeating(arr, n, k))
