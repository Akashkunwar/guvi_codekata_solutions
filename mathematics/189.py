# QID: 189
# 
# A number is given as input.Find the maximum number that can be formed using the digits.
# Input Size : N <= 10000000 
# 
# 
# Sample Testcase :
# INPUT
# 4123
# OUTPUT
# 4321
# 
# 
# 
# 


# Solution:


a=input()
res = ''.join(sorted(str(a)))
a=res[::-1]
print(int(a))