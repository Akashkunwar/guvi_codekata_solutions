# QID: 837
# 
# Number is represented in linked list such that each digit corresponds to a node in linked list. Add 1 to it. For example 1999 is represented as (1-> 9-> 9 -> 9) and adding 1 to it should change it to (2->0->0->0)
# 
# First line consists of length of the linked list.
# Second line consists the linked list each node in the linked list are having numbers as their data(separated by space).
# 
# Print the linked list after adding 1 to it(separated by space)
# 
# Sample Input : 
# 4
# 1 9 9 9
# 
# Sample Output : 
# 2 0 0 0
# 


# Solution:


a = input()
b = ''
c = [str(i) for i in input().split()]
for x in c:
    b = b+x
b = int(b)
b = b+1
b = str(b)
d = list(b)
e = []
for x in d:
  e.append(int(x))
print(*e)