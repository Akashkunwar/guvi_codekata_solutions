# QID: 983
# 
# Given a number n,a,b and c Find the number n is divisible by a,b,c if divisible print yes else print no
# 
# Given number n,a,b and c separated by a space
# 0<n<1000
# 0<a<1000
# 0<b<1000
# 0<c<1000
# 
# Print yes or no
# 
# Sample Input : 
# 3 5 8 9
# 
# Sample Output : 
# no
# 


# Solution:


a = [int(i) for i in input().split()]
b = []
for x in a:
  if a[0]%x==0:
    b.append('yes')
  else:
    b.append('no')
if 'no' in b:
  print('no')
else:
  print('yes')