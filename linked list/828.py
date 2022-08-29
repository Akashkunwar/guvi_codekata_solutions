# QID: 828
# 
# Given a linked list,reverse it and print the values of linked list after reversed.
# 
# 
# 
# First line represents the size of the linked list
# .Next line represents the sequence of numbers as the node value of the linked list(separated by space).
# 
# Print the resultant of reversed linked list value(separated by space)
# 
# Sample Input : 
# 4
# 1 2 3 4
# 
# Sample Output : 
# 4 3 2 1
# 


# Solution:


a=input()
a1 = [int(i) for i in input().split(" ")]
print(*a1[::-1], sep = " ")