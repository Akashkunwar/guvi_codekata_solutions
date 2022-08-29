# QID: 45
# 
# Given 2 numbers N,K followed by N elements print all the elements lesser than K in sorted order.If the elements could not be found print -1
# Input Size : N <= 100000
# 
# 
# Sample Testcase :
# INPUT
# 5 3
#  1 2 1 4 1
# OUTPUT
# 1 1 1 2
# 
# 
# 
# 


# Solution:


a,b = input().split()
c = [int(i) for i in input().split()]
d = []
b = int(b)
for x in c:
    if x<b:
        d.append(x)
    else:
        pass

if len(d)>0:
    d.sort()
    print(*d)
else:
    print(-1)
