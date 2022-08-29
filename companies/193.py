# QID: 193
# 
# Roman Reigns want to identify the repeated letters in two given strings and capitalize it.Help him to achieve it.
# 
# 
# Sample Testcase :
# INPUT
# computer program
# OUTPUT
# cOMPuteR PROgRaM
# 
# 
# 
# 


# Solution:


a = list(input())
try:
  # a.remove(' ')
  b = []
  for x in a:
    b.append(a.count(x))
  t = -1
  g = []
  for x in b:
    t = t+1
    if x==1:
      g.append(a[t])
  # print(*g,sep='')
except:
  a=list(a)
  b = sorted(set(a), key=lambda x: a.index(x))
  # print(*b,sep='')

o = []
for x in a:
  if x in g:
    o.append(x)
  else:
    o.append(x.upper())
print(*o,sep='')