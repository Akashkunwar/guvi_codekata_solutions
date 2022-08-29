# QID: 13
# 
# Given 2 numbers N,M. Print 'yes' if  their product is a perfect square else print 'no'.
# 
# 
# Sample Testcase :
# INPUT
# 5 5
# OUTPUT
# yes
# 
# 
# 
# 


# Solution:


import math
def isPerfectSquare(x):
    if(x >= 0):
        sr = int(math.sqrt(x))
        return ((sr*sr) == x)
    return false
a,b = map(int, input().split(" "))
x=a*b
if (isPerfectSquare(x)):
    print("yes")
else:
    print("no")