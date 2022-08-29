# QID: 190
# 
#  Given two strings S1 and S2,display 'yes' if given two strings are complementary otherwise display 'no'. If we join alphabets of both the strings we should get all 26 capital letters exactly once, then only we can call them as complementary.
# 
# 
# Sample Testcase :
# INPUT
# ABDCFGIJKLMNOPQUVWXYZ
# EHRST
# OUTPUT
# yes
# 
# 
# 
# 


# Solution:


a = list(set(list(input())))
b = list(set(list(input())))
c = a+b
if len(c) == 26:
  print('yes')
else:
  print('no')