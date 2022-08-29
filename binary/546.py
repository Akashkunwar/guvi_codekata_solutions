# QID: 546
# 
# You are given a large number made of only 0s and 1s.Your task is to find the max no of consecutive 1s. If there are no 1s print -1
# 
# A large number ‘n’
# 
# 
# Print the max no of consecutive 1 in the number
# 
# 
# Sample Input : 
# 101011111
# 
# 
# Sample Output : 
# 5
# 


# Solution:


a = input()
b = 0
c = 0
for x in a:
  if x == '1':
    c = c+1
  else:
    if c>b:
      b = c
      c = 0
    else:
      c = 0
if c>b:
  b = c
  c = 0
else:
  c = 0
if b==0:
  print(-1)
else:
  print(b)