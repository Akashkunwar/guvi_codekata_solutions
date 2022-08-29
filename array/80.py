# QID: 80
# 
# Given a string S, print the encoded string by adding 3 to each character(a maps to d,b maps to e,c maps to f and so on).
# Input Size : 1 <= N <= 100000
# 
# 
# Sample Testcase :
# INPUT
# RADAR
# OUTPUT
# UDGDU
# 
# 
# 
# 


# Solution:


s = input()
L = []
for c in s :
    k = ord(c) + 3
    if k > ord('Z') : k -= 26
    L.append(chr(k))
s2 = ''.join(L)
print(s2)