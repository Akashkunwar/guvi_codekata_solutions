# QID: 1013
# 
# Given a string print the duplicate in the string  if their no duplicate  print -1
# 
# Given a string
# 
# Print duplicate of the string  or -1
# 
# Sample Input : 
# Guvi Geek
# 
# Sample Output : 
# Ge
# 


# Solution:


a = [str(i) for i in input()]
b = ''
for x in a:
  if a.count(x)>1:
    b = b+x
  else:
    pass
b = list(set(b))
c = ''
for x in b:
  c = c+x
if len(c)>0:
  print(c)
else:
  print(-1)