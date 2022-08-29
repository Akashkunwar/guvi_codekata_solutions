# QID: 206
# 
# Given a number N and array of N integers, print the difference between the indices of smallest and largest number(if there are multiple occurances, consider the first occurance).
# Input Size : |N| <= 1000000
# 
# 
# Sample Testcase :
# INPUT
# 5
# 3 5 4 4 7
# OUTPUT
# 4
# 
# 
# 
# 


# Solution:


a = input()
a1 = [int(i) for i in input().split(" ")]
b = max(a1)
c = min(a1)
print(a1.index(b)-a1.index(c))