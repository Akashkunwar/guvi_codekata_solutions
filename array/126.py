# QID: 126
# 
# Given a range[L,R], print the sum of all the odd numbers within the range(inclusive of L and R).
# Sample Testcase:
# INPUT
# 5 10
# OUTPUT
# 21
# 
# 
# 
# 


# Solution:


def sumOdd(n):
	terms = (n + 1)//2
	sum1 = terms * terms
	return sum1
def suminRange(l, r):
	return sumOdd(r) - sumOdd(l - 1)
l,r = map(int,input().split(" "))
print(suminRange(l, r))