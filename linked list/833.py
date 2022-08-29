# QID: 833
# 
# Delete the N-th node from the end of the linked list
# 
# 
# 
# First line represents the size of the linked list.
# Next line represents the sequence of numbers as the node value of the linked list(separated by space).
# Third line contains which node value to be delete
# 
# Delete the N-th Node from the last and print result the values of linked list(separated by space).
# 
# Sample Input : 
# 5
# 1 2 3 4 5
# 3
# 
# Sample Output : 
# 1 2 4 5
# 


# Solution:


aa = input()
a = [int(i) for i in input().split()]
a = a[::-1]
b = int(input())
a.pop(b-1)
print(*a[::-1])