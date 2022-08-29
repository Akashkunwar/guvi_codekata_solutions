# QID: 297
# 
# Given a string S of length N, reverse every word in place.
# Input Size : 1 <= N <= 100000
# 
# 
# Sample Testcase :
# INPUT
# abcd er x
# OUTPUT
# dcba re x
# 
# 
# 
# 


# Solution:


a = list(input().split())
b = []
for x in a:
  b.append(x[::-1])
print(*b)