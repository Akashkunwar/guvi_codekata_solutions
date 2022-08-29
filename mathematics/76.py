# QID: 76
# 
# Given a number N and an array of N elements, every number is repeated except for one. Print that one number.
# Input Size : 1 <= N <= 100000
# 
# 
# Sample Testcase :
# INPUT
# 10
# 1 2 3 2 3 3 2 5 5 2
# OUTPUT
# 1
# 
# 
# 
# 


# Solution:


aa = input()
a = [int(i) for i in input().split(" ")]
print(min(a[::-1], key=a.count))