# QID: 834
# 
# Merge two sorted linked lists and print the new merged linked list.
# 
# The new list should be made by splicing together the nodes of the first two lists, and should also be sorted.
# 
# Given two sorted linked list of size M,N 
# First line M is the size of the first sorted linked list,
# Second line N is the size of the first sorted linked list.
# Third and Fourth line contains respective linked list values(separated by space)
# 
# Print the resultant linked list after merging the two sorted linked list(separated by space)
# 
# Sample Input : 
# 3
# 3
# 5 8 20
# 4 11 15
# 
# Sample Output : 
# 4 5 8 11 15 20
# 


# Solution:


aa = input()
aaa = input()
a = [int(i) for i in input().split(" ")]
b = [int(i) for i in input().split(" ")]
a1 = sorted(a+b)
print(*a1, sep = " ")