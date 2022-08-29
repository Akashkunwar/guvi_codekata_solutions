# QID: 275
# 
# Given a string S and a number K. Print all the substrings of S of length K(space separeted output).
# Input Size : |S| <= 100 and K<= 50
# 
# 
# Sample Testcase :
# INPUT
# prog 2
# OUTPUT 
# pr ro og
# 
# 
# 
# 


# Solution:


a,b = input().split(' ')
b = int(b)
c = list(range(0,len(a)))

d = []
try:
  for x in c:
    e = a[x:x+b]
    if len(e)==b:
      d.append(e)
except:
  pass
print(*d)