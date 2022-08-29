# QID: 982
# 
# Given a number n Find whether the number is divisible  by 2,3 and 5.if divisible print yes else print no
# 
# 0<n<1000
# Given a number n
# 
# Print yes or no
# 
# Sample Input : 
# 30
# 
# Sample Output : 
# yes
# 


# Solution:


aa = int(input())
a = [2,3,5]
b = []
for x in a:
  if aa%x==0:
    b.append('yes')
  else:
    b.append('no')
if 'no' in b:
  print('no')
else:
  print('yes')