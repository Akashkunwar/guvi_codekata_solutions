# QID: 998
# 
# Given a numbers n  followed by x and y array of n numbers add the array x and y and print the numbers
# 
# 0<n<100
# Given a number n 
# Followed by n number in next line
# Followed by n number in next line
# 
# Print added n numbers
# 
# Sample Input : 
# 6
# 5 7 4 4 6 8
# 1 2 3 5 1 1
# 
# Sample Output : 
# 6 9 7 9 7 9
# 


# Solution:


a = input()
b = [int(i) for i in input().split()]
c = [int(i) for i in input().split()]
import numpy as np
b = np.array(b)
c = np.array(c)
d = b+c
print(*d)