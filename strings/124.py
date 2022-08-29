# QID: 124
# 
# Given a number N, print the kth digit from the given position p(given order N P K).
# 
# 
# Sample Testcase :
# INPUT
# 5765 2 1
# OUTPUT
# 6
# 
# 
# 
# 


# Solution:


a,b,c=map(str,input().split(" "))
d = int(b)+int(c)
e = a[d-1]
print(e)