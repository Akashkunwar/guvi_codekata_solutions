# QID: 51
# 
# Given a string two strings S1 and S2, remove characters from the S1 which are present in the S2.If S1 becomes empty then print -1
# Input Size : N <= 100000 
# 
# 
# Sample Testcase :
# INPUT
# GUVI GEEK
# OUTPUT
# UVI
# 
# 
# 
# 


# Solution:


a,b = input().split()
a = list(a)
b = list(b)
c = []
for x in a:
  if x not in b:
    c.append(x)
if len(c)==0:
  print(-1)
else:
  print(*c, sep="")