# QID: 59
# 
# Given an array, find the maximum difference between any two elements.
# Input Size : N <= 1000000(complexity O(n) or O(nlogn))
# 
# 
# Sample Testcase :
# INPUT
# 5
# 1 2 3 4 5
# OUTPUT
# 4
# 
# 
# 
# 


# Solution:


a = input()
b = [int(i) for i in input().split()]
c = max(b) - min(b)
print(c)