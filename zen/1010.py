# QID: 1010
# 
# Given a string convert string into camel case
# 
# Given a string
# 
# Print string into camel case
# 
# Sample Input : 
# guvi geek
# 
# Sample Output : 
# guviGeek
# 


# Solution:


a = [i for i in input().split()]
b = a[1:]
c = a[0]
for x in b:
  c=c+x.capitalize()
print(c)