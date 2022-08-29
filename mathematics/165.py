# QID: 165
# 
# Given a number N, check whether it is a power of 2.
# 
# 
# Sample Testcase :
# INPUT
# 2048
# OUTPUT
# yes
# 
# 
# 
# 


# Solution:


# Python program to check if given
# number is power of 2 or not

# Function to check if x is power of 2
def isPowerOfTwo (x):

	# First x in the below expression
	# is for the case when x is 0
	return (x and (not(x & (x - 1))) )
num = int(input())
# Driver code
if(isPowerOfTwo(num)):
	print('yes')
else:
	print('no')

# This code is contributed by Danish Raza
