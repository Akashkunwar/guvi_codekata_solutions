# QID: 831
# 
# Given a linked list delete the given number node in the linked list without using a head pointer.
# 
#  
# 
# First line represents the size of the linked list.
# Next line contains characters of a linked list(separated by space).Third line contains the node that has to be deleted.
# 
# Print the values of linked list after deleting the node(separated by space).
# 
# Sample Input : 
# 6
# 1 2 3 4 5 6
# 3
# 
# Sample Output : 
# 1 2 4 5 6
# 


# Solution:


a = input()
a = [int(i) for i in input().split()]
b = int(input())
a.remove(b)
print(*a)