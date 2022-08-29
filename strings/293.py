# QID: 293
# 
# Given a string S of length N, reverse the words at odd positions.
# Input Size: 1 <= N <= 100000
# 
# 
# Sample Testcase :
# INPUT
# This is an example for this question
# OUTPUT
# sihT is na example rof this noitseuq
# 
# 
# 
# 


# Solution:


a = list(input().split())
b = []
for x in a:
  if a.index(x)%2==0:
    b.append(x[::-1])
  else:
    b.append(x)
print(*b)