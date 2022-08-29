# QID: 187
# 
# Given a string, print the run-length encoded output.
# Input Size : N <= 100000
# 
# 
# Sample Testcase :
# INPUT
# aaab
# OUTPUT
# a3b1
# 
# 
# 
# 


# Solution:


a = input()
b = ''
c = 0
for x in a:
  if len(b)==0:
    b = b+a[0]
    c = c+1
  elif x==b[-1]:
    c = c+1
  elif x!=b[-1]:
    b = b+str(c)
    c = 0
    b = b+x
    c = c+1
b = b+str(c)
print(b)