# QID: 112
# 
# Given a number N and an array of N elements, find the Bitwise OR of the array elements.
# Input Size : N <= 100000
# 
# 
# Sample Testcase :
# INPUT
# 2
# 2 4
# OUTPUT
# 6
# 
# 
# 
# 


# Solution:


from functools import reduce
a = input()
test_list = [int(i) for i in input().split(" ")]
res = reduce(lambda x, y: x | y, test_list)
print(str(res))