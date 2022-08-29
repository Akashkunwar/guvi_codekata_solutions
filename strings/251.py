# QID: 251
# 
# Given a string S of length N, print all permutations of the string in a separate line.
# Input Size : 1 <= N <= 100000
# Sample Testcases :
# INPUT
# 123
# OUTPUT
# 123
# 231
# 321
# 213
# 312
# 132
# 
# 
# 
# 


# Solution:


def toString(List):
	return ''.join(List)
def permute(a, l, r):
	if l==r:
		print (toString(a))
	else:
		for i in range(l,r+1):
			a[l], a[i] = a[i], a[l]
			permute(a, l+1, r)
			a[l], a[i] = a[i], a[l]
string = input()
n = len(string)
a = list(string)
permute(a, 0, n-1)
