# QID: 44
# 
# Given a number N and 2 arrays A and B of sorted order of size N, print the common elements.If it is not found print -1.
# Input Size : 1 <= N <= 100000
# 
# 
# Sample Testcase :
# INPUT
# 5
# 1 1 1 1 1
# 1 2 3 4 5
# OUTPUT
# 1
# 
# 
# 
# 


# Solution:


aa = input()
a = [int(i) for i in input().split(" ")]
b = [int(i) for i in input().split(" ")]
c = list(set(a).intersection(b))
c = sorted(c)
if len(c)==0:
  print(-1)
else:
  print(*c,sep=" ")