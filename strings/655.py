# QID: 655
# 
# you are given with two strings.Your task is to check whether one of the string is substring of the other.If substring exists,then print the starting index of sub-string.
# 
# You are given two strings
# 
# 
# Print the index of string if substring exists else print -1
# 
# Sample Input : 
# Yuvi
# Yuvirat
# 
# 
# Sample Output : 
# 1
# 


# Solution:


a = input()
b = input()
c = 0
if a in b:
  c = b.index(a[0])
elif b in a:
  c = a.index(b[0])
else:
  c = -2
print(c+1)