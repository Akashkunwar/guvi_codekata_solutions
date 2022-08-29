# QID: 972
# 
#  Given a number n followed by n numbers print the number which is greater than 15 if there is no number exits print -1
# 
# 0<n<100
# Given a number n 
# Followed by n number in next line
# 
# Print the number which is greater than 15 if there is no number exits print -1
# 
# Sample Input : 
# 3
# 5 7 4
# 
# Sample Output : 
# -1
# 


# Solution:


a = input()
b = [int(i) for i in input().split()]
c = []
for x in b:
    if x>15:
        c.append(x)
    else:
        pass
if len(c)==0:
    print(-1)
else:
    print(*c)