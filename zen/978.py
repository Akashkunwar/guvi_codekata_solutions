# QID: 978
# 
# Given a number n followed by n numbers Find the sum of the elements in an array
# 
# 0<n<100
# Given a number n 
# Followed by n number in next line
# 
# Print the sum of the elements in an array
# 
# Sample Input : 
# 3
# 5 7 4
# 
# Sample Output : 
# 16
# 


# Solution:


a = input()
b = [int(i) for i in input().split()]
print(sum(b))