# QID: 142
# 
# Accept a string and find if it is of date format 'dd/mm/yyyy'.
# 
# 
# Sample Testcase :
# INPUT
# 01/13/1999
# OUTPUT
# no
# 
# 
# 
# 


# Solution:


a,b,c=input().split('/')
a = int(a)
b = int(b)
c = len(c)

x = list(range(1,32))
y = list(range(1,13))

d = []
if a in x:
  d.append(1)
else:
  d.append(0)

if b in y:
  d.append(1)
else:
  d.append(0)

if c == 4:
  d.append(1)
else:
  d.append(0)

if sum(d)==3:
  print('yes')
else:
  print('no')