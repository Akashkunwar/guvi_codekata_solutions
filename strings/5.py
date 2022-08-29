# QID: 5
# 
# Given a string S, print 'yes' if it is a palindrome or 'no' if it is not a palindrome.
# 
# 
# Sample Testcase :
# INPUT
# lappal
# OUTPUT
# yes
# 
# 
# 
# 


# Solution:


a = input()
b = len(a)
if b%2!=0:
  c = int((b+1)/2)
  r = list(range(c,b))
  l = list(range(c-2,-1,-1))
  d = []
  e = []
  for x in r:
    d.append(a[x])
  for y in l:
    e.append(a[y])
elif b%2==0:
  b = len(a)
  c = int(b/2)
  r = list(range(c,b))
  l = list(range(c-1,-1,-1))
  b = 0
  d = []
  e = []
  for x in r:
    d.append(a[x])
  for y in l:
    e.append(a[y])
else:
  pass
if d==e:
  print("yes")
else:
  print("no")