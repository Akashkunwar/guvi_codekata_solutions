# QID: 8
# 
# Given a floating point number with 1 decimal place round it off to nearest greater integer and print it.
# 
# 
# Sample Testcase :
# INPUT
# 2.6
# OUTPUT
# 3
# 
# 
# 
# 


# Solution:


a = float(input())
import math
print(int(math.ceil(a)))