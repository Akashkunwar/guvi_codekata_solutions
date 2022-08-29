# QID: 182
# 
# Print the position of first 1 from left to right, in binary representation of product of 2 integers after the first one.
# 
# 
# Sample Testcase :
# INPUT
# 18 2
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
c = int(bin(a)[2:])*int(bin(b)[2:])
d = list(str(c))
try:
    d[d.index('1')]='0'
    for x in d:
      if x=='1':
        print(d.index('1')+1)
except:
    print(0)