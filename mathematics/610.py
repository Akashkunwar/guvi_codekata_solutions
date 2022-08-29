# QID: 610
# 
# :You are given an array of n numbers.your task is to print the lcm of n numbers
# 
# An integer ‘n’ denoting the size of array.Next line contains ‘n’ space separated numbers
# 
# 
# Print the lcm
# 
# 
# Sample Input : 
# 4
# 2 4 6 8
# 
# 
# Sample Output : 
# 24
# 


# Solution:


def __gcd(a, b):
	if (a == 0):
		return b
	return __gcd(b % a, a)

def LcmOfArray(arr, idx):

	if (idx == len(arr)-1):
		return arr[idx]
	a = arr[idx]
	b = LcmOfArray(arr, idx+1)
	return int(a*b/__gcd(a,b))
aa = input()
arr = [int(i) for i in input().split(" ")]
print(LcmOfArray(arr, 0))
