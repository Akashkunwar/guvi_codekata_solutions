# QID: 208
# 
# Given a string S, retain the character(s) once irrespective of number of times it occurs in the given string.
# Input Size : |S| <= 100000
# 
# 
# Sample Testcase :
# INPUT
# aabbaa
# OUTPUT
# ab
# 
# 
# 
# 


# Solution:


a = list(set(list(input())))
a = sorted(a)
print(*a,sep="")