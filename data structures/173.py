# QID: 173
# 
# Given 2 numbers a and B.Print the value of a!/b!.
# Input Size : A,B <= 10000 and A-B <= 5
# 
# 
# Sample Testcase :
# INPUT
# 4 2
# OUTPUT
# 12
# 
# 
# 
# 


# Solution:


a,b = input().split()
a = int(a)
b = int(b)
aa = 1
for x in range(1,a+1):
  aa = aa*x
bb = 1
for y in range(1,b+1):
  bb = bb*y
print(int(aa/bb))