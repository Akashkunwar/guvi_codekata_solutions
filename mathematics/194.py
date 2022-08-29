# QID: 194
# 
# Given 2 numbers, perform bitwise xor and find the number of ones in its binary representation.
# 
# 
# Sample Testcase :
# INPUT
# 10 5
# OUTPUT
# 4
# 
# 
# 
# 


# Solution:


a,b = input().split()
a = int(a)
b = int(b)
c = a^b
d = bin(c)[2:]
e = 0
for x in d:
  if x=='1':
    e+=1
  else:
    pass
print(e)