# QID: 200
# 
# Given 2 arrays print 'yes' if they are mirror images of each other,otherwise 'no'.
# Input Size : N <= 1000000
# 
# 
# Sample Testcase :
# INPUT
# 4
# 1 2 3 4
# 4 3 2 1
# OUTPUT
# yes
# 
# 
# 
# 


# Solution:


a = input()
a1 = [int(i) for i in input().split(" ")]
a2 = [int(i) for i in input().split(" ")]
b1 = a2[::-1]
if a1==b1:
  print("yes")
else:
  print("no")