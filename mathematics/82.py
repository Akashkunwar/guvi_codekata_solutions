# QID: 82
# 
# Given a number N and a number K, find the greatest number which divides both.
# Input Size : N and K <= 100000
# 
# 
# Sample Testcase :
# INPUT
# 5 10
# OUTPUT
# 5
# 
# 
# 
# 


# Solution:


def hcfnaive(a,b):
	if(b==0):
		return a
	else:
		return hcfnaive(b,a%b)
a,b= map(int,input().split(" "))
print(hcfnaive(a,b))