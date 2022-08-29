# QID: 23
# 
# Given a number N, print the product of the digits.
# Input Size : N <= 100000000000
# 
# 
# Sample Testcase :
# INPUT
# 2143
# OUTPUT
# 24
# 
# 
# 
# 


# Solution:


# Python3 program to compute
# product of digits in the number.

# Function to get product of digits
def getProduct(n):

	product = 1

	while (n != 0):
		product = product * (n % 10)
		n = n // 10

	return product

# Driver Code
n = int(input())
print(getProduct(n))

# This code is contributed
# by mohit kumar
