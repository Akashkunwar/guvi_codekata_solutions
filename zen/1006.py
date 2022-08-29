# QID: 1006
# 
# Given a string print the vowels in the string
# 
# Given a string
# 
# Print the String
# 
# Sample Input : 
# guvi geek
# 
# Sample Output : 
# ui ee
# 


# Solution:


a = input()
b = ''
for x in a:
  if x=='a' or x==' ' or x=='e' or x=='i' or x=='o' or x=='u':
    b = b+x
  else:
    pass
print(b)