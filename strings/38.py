# QID: 38
# 
# Given a string 'S' and a character 'K', find how many times 'K' got repeated in 'S'.If 'K' is not found in 'S' print -1
# Input Size : |s| <= 100000
# 
# 
# Sample Testcase :
# INPUT
# codekata a
# OUTPUT
# 2
# 
# 
# 
# 


# Solution:


a,b = input().split()
c = 0
for x in a:
  if a[a.index(x)] == b:
    c = c+1
  else:
    pass
if c==0:
  print(-1)
else:
  print(c)