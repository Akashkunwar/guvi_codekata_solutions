# QID: 96
# 
# Given a string, print the least repeated characters in the string.If there are more than one character repeated preserve the order as in the input.
# Input Size : 1 <= N <= 100000
# 
# 
# Sample Testcase :
# INPUT
# codeKata challenge
# OUTPUT
# odKthng
# 
# 
# 
# 


# Solution:


a = list(input())
try:
  a.remove(' ')
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
except:
  a=list(a)
  b = sorted(set(a), key=lambda x: a.index(x))
  print(*b,sep='')