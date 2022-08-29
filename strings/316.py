# QID: 316
# 
# Given a string S, remove the characters which exist more than one times,and print the remaining string.
# Input Size : |S| <= 10000000
# 
# 
# Sample Testcase :
# INPUT
# Engineering
# OUTPUT
# Er
# 
# 
# 
# 


# Solution:


a = list(input())
b = []
for x in a:
  b.append(a.count(x))
t = -1
g = []
for x in b:
  t = t+1
  if x==1:
    g.append(a[t])
print(*g,sep='')