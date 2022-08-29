# QID: 992
# 
# Given a number n followed by n numbers Print the index 2nd  largest number in an array (1 base index)
# 
# 0<n<100
# Given a number n 
# Followed by n number in next line
# 
# Print the largest number index in an array
# 
# 
# Sample Input : 
# 6
# 5 7 4 4 6 8
# 
# Sample Output : 
# 2
# 


# Solution:


a = input()
b = [int(i) for i in input().split()]
c = b.copy()
c.sort()
if c[-1]!=c[-2]:
    d = c[-2]
else:
    d = c[-3]
print(b.index(d)+1)