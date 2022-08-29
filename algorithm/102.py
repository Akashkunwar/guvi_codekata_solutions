# QID: 102
# 
# Given a number N, followed by an array of N elements,print 'yes' if it is a sorted array(either ascending or descending)otherwise print 'no'.
# Input Size : 1 <= N <= 100000
# 
# 
# Sample Testcase :
# INPUT
# 3
# 2 3 7
# OUTPUT
# yes
# 
# 
# 
# 


# Solution:


a = int(input())
b = [int(i) for i in input().split()]
c = sorted(b)
d = c[::-1]
if b == c or b == d:
  print('yes')
else:
  print('no')