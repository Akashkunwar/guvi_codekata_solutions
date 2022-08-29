# QID: 979
# 
# Given a number n followed by n numbers Find the sum of the elements in an array and print sum of number is odd or even
# 
# 0<n<100
# Given a number n 
# Followed by n number in next line
# 
# print sum of number is odd or even
# 
# Sample Input : 
# 3
# 5 7 4
# 
# Sample Output : 
# even
# 


# Solution:


a = input()
b = [int(i) for i in input().split()]
c = sum(b)
if c%2==0:
    print('even')
else:
    print('odd')