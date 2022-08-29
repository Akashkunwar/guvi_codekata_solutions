# QID: 840
# 
# Given a linked list and a key,find the last occurrence of the key and delete it from the linked list. The list may have duplicate values.
# 
# First line represents the size of the linked list.
# Next line represents the sequence of numbers as the node value of the linked list(separated by space).
# Third line contains the key to be deleted
# 
# Print the resultant linked list(separated by space).
# 
# Sample Input : 
# 6
# 1 21 3 5 21 10
# 21
# 
# Sample Output : 
# 1 21 3 5 10
# 


# Solution:


a = input()
a = [int(i) for i in input().split()]
a = a[::-1]
b = int(input())
a.remove(b)
a = a[::-1]
print(*a)