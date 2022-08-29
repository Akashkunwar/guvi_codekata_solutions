# QID: 975
# 
#  Given a number n,m and k separated by a space followed by n numbers print the numbers between this two numbers listed in a array if there is no number exits print -1
# 
# number n, m and k separated by a space
# 0<n<1000
# 0<m<1000
# 0<k<1000
# m<k
# Given a number n 
# Followed by n number in next line
# 
# 
# print the numbers between this two numbers listed in a array if there is no number exits print -1
# 
# Sample Input : 
# 3 5 8
# 5 7 4
# 
# Sample Output : 
# 7
# 


# Solution:


a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
c = []
for x in b:
    if x in range(a[1]+1,a[2]):
        c.append(x)
    else:
        pass
if len(c)==0:
    print(-1)
else:
    print(*c)