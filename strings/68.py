# QID: 68
# 
# Given a string/sentence print its corresponding camelcase convention.
# Input Size : |s| <= 1000000(complexity O(n))
# 
# 
# Sample Testcase :
# INPUT
# guvi geeks
# OUTPUT
# GuviGeeks
# 
# 
# 
# 


# Solution:


a = [str(i).capitalize() for i in input().split(' ')]
print(*a,sep='')