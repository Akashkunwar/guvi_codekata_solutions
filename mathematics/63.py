# QID: 63
# 
# Given a String S,print the number of unique characters in it.If all the characters are duplicated,then print -1.
# 
# 
# Sample Testcase :
# INPUT
# GUVIGEEK
# OUTPUT
# 4
# 
# 
# 
# 


# Solution:


a = input()
a = list(a)
b = []
c = 0
for x in a:
  b.append(a.count(x))
for x in b:
  if x==1:
    c = c+x
  else:
    pass
if c>0:
  print(c)
else:
  print(-1)