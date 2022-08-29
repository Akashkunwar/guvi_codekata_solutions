# QID: 166
# 
# Given a number N, find the number of ones in its binary representation.
# 
# 
# Sample Testcase :
# INPUT
# 276
# OUTPUT
# 3
# 
# 
# 
# 


# Solution:


a = list(bin(int(input()))).count("1")
print(a)