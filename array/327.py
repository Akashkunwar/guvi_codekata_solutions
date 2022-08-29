# QID: 327
# 
# Given a number N and N strings of length atmost M, print the longest common prefix.
# Input Size : 1<=N, M<=100000
# Example:
# INPUT
# 2
# Vishal
# Vidharba
# OUTPUT
# Vi
# 
# 
# 
# 


# Solution:


a = int(input())
a = input()
b = input()
c = []
for x,y in zip(a,b):
  if x==y:
    c.append(x)
  else:
    break
print(*c,sep='')