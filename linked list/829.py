# QID: 829
# 
# Given a linked list,rotate it for a given number of times and print the values of linked list after rotation.
# 
# First line represents the size of the linked list.
# Next line represents the sequence of numbers as the node value of the linked list(separated by space).
# Third line contains the number of rotations to be done.
# 
# Print the resultant rotated linked list value(separated by space).
# 
# Sample Input : 
# 8
# 1 2 3 4 5 6 7 8
# 4
# 
# Sample Output : 
# 5 6 7 8 1 2 3 4
# 


# Solution:


aa = input()
a = [int(i) for i in input().split()]
b = int(input())
a = a[::-1]
c = a[:b][::-1]
d = a[b:][::-1]
e = c + d
print(*e)