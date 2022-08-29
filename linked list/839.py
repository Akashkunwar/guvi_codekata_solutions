# QID: 839
# 
# Delete the middle node of a linked list and print the resulting linked list.
# 
# First line represents the size of the linked list.
# Next line represents the sequence of numbers as the node value of the linked list.
# 
# Print the resultant linked list.
# 
# Sample Input : 
# 4
# 45 56 67 78
# 
# Sample Output : 
# 45 67 78
# 


# Solution:


a = int(input())
b = [int(i) for i in input().split()]
c = a//2
b.pop(c-1)
print(*b)