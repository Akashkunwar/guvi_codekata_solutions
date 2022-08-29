# QID: 836
# 
# Given a singly linked list consisting of N nodes. The task is to remove duplicates (nodes with duplicate values) from the given list (if exists).
# 
# First line of input contains length of linked list and next line contains the linked list data(separated by space).
# 
# Single line of output which contains linked list with no duplicates(separated by space).
# 
# Sample Input : 
# 4
# 2 2 4 5
# 
# Sample Output : 
# 2 4 5
# 


# Solution:


a = input()
test_list = [int(i) for i in input().split(" ")]
test_list = list(set(test_list))
print(*test_list, sep = " ")