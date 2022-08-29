# QID: 18
# 
# Given 2 numbers N,M find the GCD of N and M.If it cannot be found for given number(s) then print -1
# 
# 
# Sample Testcase :
# INPUT
# 10 5
# OUTPUT
# 5
# 
# 
# 
# 


# Solution:


a,b = map(int, input().split(" "))
import numpy as np
if (a==0 or b==0):
    print(-1)
else:
    c = np.gcd(a,b)
    print(c)