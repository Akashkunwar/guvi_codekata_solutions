# QID: 1000
# 
# Given a string find the length of the string without space
# 
# Given a string
# 
# Print length in number
# 
# Sample Input : 
# guvi geek
# 
# Sample Output : 
# 8
# 


# Solution:


a = input()
b = ''
for x in a:
  if x!=' ':
    b = b+x
  else:
    pass
print(len(b))