# QID: 988
# 
# Given a number n followed by n numbers Print the smallest number in an array
# 
# 0<n<100
# Given a number n 
# Followed by n number in next line
# 
# Print the smallest number in an array
# 
# Sample Input : 
# 6
# 5 7 4 4 6 8
# 
# Sample Output : 
# 4
# 


# Solution:


a = input()
b = [int(i) for i in input().split()]
print(min(b))