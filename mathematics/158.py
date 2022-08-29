# QID: 158
# 
#  A number is given as input. Find the odd digits in the number, add them and find if the sum is odd or not. If even print E, if odd print O.
# Input Size : N <= 10000000000
# 
# 
# Sample Testcase :
# INPUT
# 413
# OUTPUT
# E
# 
# 
# 
# 


# Solution:


a = list(input())
b = []
for x in a:
  if int(x)%2!=0:
    b.append(int(x))
  else:
    pass
if sum(b)%2==0:
  print('E')
else:
  print('O')