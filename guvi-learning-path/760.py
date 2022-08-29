# QID: 760
# 
# Write a program to rotate the given string by the given number of times.
# 
# String, rotation times
# 
# print the Rotated string
# 
# Sample Input : 
# hello 3
# 
# Sample Output : 
# llohe
# 


# Solution:


a,b = input().split()
b = int(b)
for x in range(0,b):
  a = a[-1] + a[:-1]
print(a)