# QID: 135
# 
# Given a number N and an array of N elements, print the array after removing duplicate elements.If no duplicate elements found print the same.
# Input Size :  N <= 100000
# 
# 
# Sample Testcase :
# INPUT
# 4
# 2 4 4 2
# OUTPUT
# 2 4
# 
# 
# 
# 


# Solution:


a = input()
b = [int(i) for i in input().split(" ")]
c = list(set(b))
print(*c, sep = " ")