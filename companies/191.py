# QID: 191
# 
# Swagger and Rock are playing a word game. They need to check the two strings use the same base alphabets. Two strings are said to have same base alphabets if they use the same characters to form the word. eg: rescue and curse have same base alphabets - c,e,r,s,u.If it so print 'true' else print 'false'.
# Input Size : |S| <= 1000000
# 
# 
# Sample Testcase :
# INPUT
# rescue curse 
# OUTPUT
# true
# 
# 
# 
# 


# Solution:


a,b = input().split()
a = list(set(list(a)))
b = list(set(list(b)))
if a==b:
  print('true')
else:
  print('false')