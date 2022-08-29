# QID: 41
# 
# Given 2 strings,check whether they have any common characters.If found print 'yes' else print 'no'.
# Input Size : |s| <= 100000(O(n))
# 
# 
# Sample Testcase :
# INPUT
# guvi guvigeeks
# OUTPUT
# yes
# 
# 
# 
# 


# Solution:


a,b = input().split(" ")
if a in b:
  print("yes")
else:
  print("no")