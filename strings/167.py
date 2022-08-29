# QID: 167
# 
# Given a string S, check whether it contains only  the characters 'a' and 'b' or only 'a' or only 'b'
# Input Size : |S| <= 100000
# 
# 
# Sample Testcase :
# INPUT
# aabbaaab
# OUTPUT
# yes
# 
# 
# 
# 


# Solution:


a = list(set(input()))
if len(a) < 3:
  for x in a:
    if x=='a' or x=='b':
      l = 'yes'
    else:
      l = 'no'
else:
  l = 'no'

print(l)