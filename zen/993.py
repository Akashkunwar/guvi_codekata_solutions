# QID: 993
# 
# Given a number n followed by n numbers Print the index 2nd  smallest number in an array (1 base index)
# 
# 0<n<100
# Given a number n 
# Followed by n number in next line
# 
# Print the smallest number index in an array
# 
# Sample Input : 
# 6
# 5 7 4 4 6 8
# 
# Sample Output : 
# 1
# 


# Solution:


a = input()
b = [int(i) for i in input().split()]
c = b.copy()
c.sort()
if c[0]!=c[1]:
    d = c[1]
else:
    d = c[2]
print(b.index(d)+1)