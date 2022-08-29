# QID: 120
# 
# Given a number N in decimal convert it into binary value.
# Input Size : N <= 100000 
# 
# 
# Sample Testcase :
# INPUT
# 5
# OUTPUT
# 101
# 
# 
# 
# 


# Solution:


def DecimalToBinary(num):
	if num >= 1:
		DecimalToBinary(num // 2)
	print(num % 2, end = '')
dec_val = int(input())
DecimalToBinary(dec_val)