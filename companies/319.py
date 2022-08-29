# QID: 319
# 
#  Given a number N, find the sum of prime numbers that end with 3 from 2 to N.
# Input Size : N <= 100000 
# 
# 
# Sample Testcase :
# INPUT
# 5
# OUTPUT
# 3
# 
# 
# 
# 


# Solution:


a = [3, 13, 23, 43, 53, 73, 83]
b = int(input())
a.append(b)
a = sorted(a)
c = a.index(b)
d = a[:c]
print(sum(d))