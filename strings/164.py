# QID: 164
# 
# Print the position of first 1 from right to left, in binary representation of an Integer.
# 
# 
# Sample Testcase :
# INPUT
# 18
# OUTPUT
# 2
# 
# 
# 
# 


# Solution:


print(int(list(bin(int(input()))[2:])[::-1].index("1"))+1)