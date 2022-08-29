# QID: 71
# 
# Given a day, print 'yes' if it is a holiday otherwise print'no'.Assume that weekend days are holidays
# 
# 
# Sample Testcase :
# INPUT
# saturday
# OUTPUT
# yes
# INPUT
# monday
# OUTPUT
# no
# 
# 
# 
# 


# Solution:


a=input()
if (a=="saturday" or a=="sunday"):
    print("yes")
else:
    print("no")