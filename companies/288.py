# QID: 288
# 
#   Given N strings and a prefix string p. Find how many of the N strings have p as their prefix.
# for eg: String[] input={'100','111','10100','10','1111'} prefix='10'
# output=2
# Input Size : N <= 100000, string length <=1000, prefix length <=100
# 
# 
# Sample Testcase :
# INPUT
# 5
# 100 111 10100 10 1111
# 10
# OUTPUT
# 3
# 
# 
# 
# 


# Solution:


a = input()
b = list(input().split())
c = input()

a = 0
d = len(c)
for x in b:
  if x[0:d] == c:
    a = a+1
  else:
    pass
print(a)