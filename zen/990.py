# QID: 990
# 
#  Given a number n followed by n numbers Print the 2nd  largest number in an array
# 
# 0<n<100
# Given a number n 
# Followed by n number in next line
# 
# Print the second largest number in an array
# 
# Sample Input : 
# 6
# 5 7 4 4 6 8
# 
# Sample Output : 
# 7
# 


# Solution:


a = input()
b = [int(i) for i in input().split()]
b = list(set(b))
b.sort()
print(b[-2])