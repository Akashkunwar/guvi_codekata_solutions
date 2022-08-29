# QID: 121
# 
# Given a number N in binary format convert it to decimal number.
# Input Size : N <= 100000 
# 
# 
# Sample Testcase :
# INPUT
# 101
# OUTPUT
# 5
# 
# 
# 
# 


# Solution:


def binaryToDecimal(n):
	num = n;
	dec_value = 0;
	base = 1;
	temp = num;
	while(temp):
		last_digit = temp % 10;
		temp = int(temp / 10);
		dec_value += last_digit * base;
		base = base * 2;
	return dec_value;
num = int(input())
print(binaryToDecimal(num));