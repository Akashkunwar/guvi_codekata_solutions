# QID: 2
# 
# Given a number N, check whether it is prime or not. Print 'yes' if it is prime else print 'no'.
# 
# 
# Sample Testcase :
# INPUT
# 123
# OUTPUT
# no
# 
# 
# 
# 


# Solution:


# Python program to check if
# given number is prime or not

num = int(input())

# If given number is greater than 1
if num > 1:

	# Iterate from 2 to n / 2
	for i in range(2, int(num/2)+1):

		# If num is divisible by any number between
		# 2 and n / 2, it is not prime
		if (num % i) == 0:
			print("no")
			break
	else:
		print("yes")

else:
	print("no")
