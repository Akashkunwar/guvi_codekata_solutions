# QID: 48
# 
# Given a number N, find the factorial of N.
# Input Size : 1 <= N <= 25
# 
# 
# Sample Testcase :
# INPUT
# 5
# OUTPUT
# 120
# 
# 
# 
# 


# Solution:


def factorial(n):
	if n == 0:
		return 1
	return n * factorial(n-1)
num = int(input())
print(factorial(num))