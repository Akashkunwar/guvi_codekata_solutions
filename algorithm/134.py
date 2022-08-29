# QID: 134
# 
# Given a number N and an array of N elements,sort the array in increasing order and print the original indices of the elements present in sorted array.
# Input Size : N <= 100000
# 
# 
# Sample Testcase :
# INPUT
# 5
# 5 4 3 2 1
# OUTPUT
# 5 4 3 2 1
# 
# 
# 
# 


# Solution:


a = input()
b = [int(i) for i in input().split(" ")]
print(*b)