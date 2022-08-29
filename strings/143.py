# QID: 143
# 
# Given 2 strings S1 and S2,work on the strings such that both string has the same number of characters.To adjust the length reduce number of exceeding characters from longer string.
# 
# 
# Sample Testcase :
# INPUT
# guvi
# geeks
# OUTPUT
# guvigeek
# 
# 
# 
# 


# Solution:


a,b = map(str,input().split(" "))
c = len(a)
d = len(b)
if c>d:
  f = a[0:d]
  print(f+b)
elif d>c:
  e = b[0:c]
  print(a+e)
else:
  print(a+b)