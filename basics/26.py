# QID: 26
# 
# Given 2 numbers N and K followed by elements of N .Print 'yes' if K exists else print 'no'.
# 
# 
# Sample Testcase :
# INPUT
# 4 2
# 1 2 3 3
# OUTPUT
# yes
# 
# 
# 
# 


# Solution:


a,b = map(int,input().split(" "))
n = [int(i) for i in input().split(" ")]
if b in n:
  print("yes")
else:
  print("no")