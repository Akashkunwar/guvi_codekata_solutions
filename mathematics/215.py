# QID: 215
# 
# Given a number N in decimal, print the length of the corresponding binary digit.
# Input Size : 1 <= N <= 100000
# 
# 
# Sample Testcase :
# INPUT
# 10
# OUTPUT
# 4
# 
# 
# 
# 


# Solution:


a = bin(int(input()))[2:]
print(len(a))