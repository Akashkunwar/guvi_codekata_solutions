# QID: 89
# 
# Given a range (i.e) two numbers L and R count the number of perfect squares within the range (inclusive of L and R).If no perfect square exists within the range print '-1'.
# Input Size : L <= R <= 100000(complexity O(n))
# 
# 
# Sample Testcase :
# INPUT
# 2 10
# OUTPUT
# 2
# 
# 
# 
# 


# Solution:


def CountSquares(a, b):

	cnt = 0
	for i in range (a, b + 1):
		j = 1;
		while j * j <= i:
			if j * j == i:
				cnt = cnt + 1
			j = j + 1
		i = i + 1
	return cnt
a,b = map(int,input().split(" "))
dd = CountSquares(a, b)
if dd==0:
    print(-1)
else:
    print(dd)