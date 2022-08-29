# QID: 7
# 
# Given 3 numbers N , L and R. Print 'yes' if N is between L and R else print 'no'.
# 
# 
# Sample Testcase :
# INPUT
# 3
# 2 6
# OUTPUT
# yes
# 
# 
# 
# 


# Solution:


a = int(input())
b,c = map(int, input().split(" "))
if (a>b and a<c):
  print("yes")
else:
  print("no")