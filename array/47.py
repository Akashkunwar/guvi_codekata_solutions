# QID: 47
# 
# Given 2 numbers N,K and an array of N elements, print the number(s) that has been repeated K times.Print them in ascending order if there are more than one number to be printed.If no element satisfies the pattern then print -1
# Input Size : N,K <= 100000 
# 
# 
# Sample Testcase :
# INPUT
# 5 2
# 1 2 4 1 2
# OUTPUT
# 1 2
# 
# 
# 
# 


# Solution:


a,b = input().split()
aa = [int(i) for i in input().split()]
b = int(b)
c = []
for x in aa:
    if aa.count(x) == b:
        c.append(x)
    else:
        pass
c = list(set(c))
if len(c)==0:
    print(-1)
else:
    print(*c)