# QID: 107
# 
# Given 3 angles A,B,C find if they can be interior angles of a triangle.If they form an interior triangle for the given angle,print 'yes' otherwise print 'no'.
# Input Size : 0 <= A,B,C <= 180
# 
# 
# Sample Testcase :
# INPUT
# 2 2 176
# OUTPUT
# yes
# 
# 
# 
# 


# Solution:


a,b,c = map(int,input().split(" "))
if a+b+c==180:
    print("yes")
else:
    print("no")