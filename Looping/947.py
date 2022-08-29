# QID: 947
# 
# Write a code to get a integer n as input and calculate the smallest perfect power of 2 greater than n.
# 
# A single line containing an integer,n.
# 
# Print the smallest perfect power of 2 greater than n.
# 
# Sample Input : 
# 48
# 
# Sample Output : 
# 64
# 


# Solution:


def perfectPowerOf2( n ):
	per_pow = 1
	while n > 0:
		per_pow = per_pow << 1
		n = n >> 1
	return per_pow
n = int(input())
print(perfectPowerOf2(n))
