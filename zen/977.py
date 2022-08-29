# QID: 977
# 
# Given a year, find whether leap year or not?
# 
# Given a 4 digit number
# 
# Print leap year or not a leap year
# 
# Sample Input : 
# 1996
# 
# Sample Output : 
# leap year
# 


# Solution:


a = int(input())
if a%4==0:
  print('leap year')
else:
  print('not a leap year')