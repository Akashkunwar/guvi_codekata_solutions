# QID: 832
# 
# Determine whether the contents in the form of linked list is a palindrome or not.
# 
# 
# 
#  
# 
# First line represents the size of the linked list.Next line contains characters in the form of a linked list(separated by space).
# 
# Print  'yes' if it forms a palindrome otherwise print 'no'.
# 
# Sample Input : 
# 5
# r a d a r
# 
# Sample Output : 
# yes
# 


# Solution:


aa = input()
a = [i for i in input().split()]
b = len(a)//2
if b%2==0:
  c = a[:b-1]
  d = a[::-1]
  d = d[:b-1]
else:
    c = a[:b-1]
    d = a[::-1]                           
    d = d[:b-1]
if c==d:
  print('yes')
else:
  print('no')