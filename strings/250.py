# QID: 250
# 
# Given a string S of length N, find whether the given string is a palindrome using stack or linked list and print 'yes' otherwise print 'no'.
# Input Size : 1 <= N <= 100000
# Sample Testcases :
# INPUT
# GuviGeek
# OUTPUT
# no
# 
# 
# 
# 


# Solution:


a = 'asdfdsa'
if len(a)%2==0:
  b = a[:len(a)//2+1]
  c = a[len(a)//2:][::-1]
else:
  b = a[:len(a)//2+1]
  c = a[len(a)//2:][::-1]

if b==c:
  print('yes')
else:
  print('no')