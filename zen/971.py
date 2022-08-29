# QID: 971
# 
# Given a number n followed by n numbers find whether it is odd or even
# 
# 0<n<100
# Given a number n 
# Followed by n number in next line
# 
# Print whether odd or even
# 
# Sample Input : 
# 3
# 5 7 4
# 
# Sample Output : 
# odd odd even
# 


# Solution:


a = input()
b = [int(i) for i in input().split()]
c = []
for x in b:
    if x%2==0:
        c.append('even')
    else:
        c.append('odd')
if len(c)==0:
    print(-1)
else:
    print(*c)