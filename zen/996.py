# QID: 996
# 
# Given a number n followed by n numbers short the n number in ascending order 
# 
#  
# 
# 0<n<100
# Given a number n 
# Followed by n number in next line
# 
# 
# Print the n number in ascending order
# 
# Sample Input : 
# 6
# 5 7 4 4 6 8
# 
# Sample Output : 
# 4 4 5 6 7 8
# 


# Solution:


a = input()
b = [int(i) for i in input().split()]
b.sort()
print(*b)