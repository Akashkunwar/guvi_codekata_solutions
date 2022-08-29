# QID: 70
# 
# Given 2 strings check whether they differ exacly by one character.If yes then print 'yes' otherwise print 'no'
# Input Size : |s| <= 100000(complexity O(nlogn) or O(n))
# 
# 
# Sample Testcase :
# INPUT
# codekata codekate
# OUTPUT
# yes
# 
# 
# 
# 


# Solution:


a,b = input().split()
a = list(a)
b = list(b)
c = []
for x,y in zip(a,b):
  if x==y:
    c.append(0)
  else:
    c.append(1)
if sum(c) == 1:
    print('yes')
else:
    print('no')