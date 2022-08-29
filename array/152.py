# QID: 152
# 
# Given a number N and an array of N integers, find the greatest number which divides all the elements of the array.
# Input Size : N <= 100000
# 
# 
# Sample Testcase :
# INPUT
# 5
# 1 2 3 4 5
# OUTPUT
# 1
# 
# 
# 
# 


# Solution:


def gcd (a, b) :
	if (a == 0) :
		return b
	
	return gcd (b % a, a)
def findNumber (arr, n) :

	ans = arr[0]
	for i in range(0, n) :
		ans = gcd (ans, arr[i])
	for i in range(0, n) :
		if (arr[i] == ans) :
			return ans
	
	return -1
	
aa = input()
arr = [int(i) for i in input().split(" ")];
n = len(arr)
print(findNumber(arr, n))