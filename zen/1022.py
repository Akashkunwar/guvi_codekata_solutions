# QID: 1022
# 
# Given a number n followed by n numbers short the n number in descending order 
# 
# 0<n<100
# Given a number n 
# Followed by n number in next line
# 
# 
# Print short the n number in descending order
# 
# Sample Input : 
# 6
# 5 7 4 4 6 8
# 
# Sample Output : 
# 8 7 6 5 4 4
# 


# Solution:


a = input()
b = [int(i) for i in input().split()]
b.sort()
b = b[::-1]
print(*b)