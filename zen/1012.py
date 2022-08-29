# QID: 1012
# 
# Given a string convert string into upper case where their vowel character
# 
# Given a string
# 
# Print string into upper case
# 
# Sample Input : 
# guvi geek
# 
# Sample Output : 
# gUvI gEEk
# 


# Solution:


a = input()
b = ''
for x in a:
  if x=='a' or x=='e' or x=='i' or x=='o' or x=='u':
    b = b + x.upper()
  else:
    b = b + x
print(b)