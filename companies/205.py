# QID: 205
# 
# How many possible ways are to shuffle given number of playing cards?.
# Input Size : |N| <= 1000000
# 
# 
# Sample Testcase :
# INPUT
# 7
# OUTPUT
# 5040
# 
# 
# 
# 


# Solution:


a = int(input())
b = 1
for x in list(range(1,a+1)):
  b*=x
print(b)