# QID: 33
# 
# Given a number N followed by N elements, find the second smallest element.If it cannot be found then print -1
# Input Size : N <= 100000 (ie do it in O(log n) time complexity)
# 
# 
# Sample Testcase :
# INPUT
# 5
# 1 2 3 4 5
# OUTPUT
# 2
# 
# 
# 
# 


# Solution:


a = input()
b = [int(i) for i in input().split()]
b = sorted(b)
if len(list(set(b))) == 1:
    print(-1)
else:
    print(b[1])