# QID: 948
# 
# Write a code to get 2 integers as input and add the integers without any carry.
# 
# A single line containing 2 integers.
# 
# Print sum of the 2 integers without carry
# 
# Sample Input : 
# 44 66
# 
# Sample Output : 
# 0
# 


# Solution:


import math
def xSum(n, m) :
	res = 0
	multiplier = 1
	bit_sum = 0
	while (n or m) :
		bit_sum = ((n % 10) +
				(m % 10))
		bit_sum = bit_sum % 10
		res = (bit_sum *
			multiplier) + res
		n = math.floor(n / 10)
		m = math.floor(m / 10)
		multiplier = multiplier * 10
	return res
n,m = map(int, input().split(" "))
print (xSum(n, m))