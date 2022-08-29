# QID: 315
# 
# Given a String S and a string P, find if P is a substring of S. Print 'yes' if it is a substring else 'no'.
# Input Size : |s| <= 10000 |p| <= 1000.
# 
# 
# Sample Testcase :
# INPUT
# sundar sun
# OUTPUT
# yes
# 
# 
# 
# 


# Solution:


a,b = input().split()
if b in a:
    print("yes")
else:
    print("no")