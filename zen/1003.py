# QID: 1003
# 
#  Given a string find the number of uppercase letters and lowercase letters
# 
# Given a string
# 
# Print the number of uppercase and lowercase
# 
# Sample Input : 
# Guvi Geek
# 
# Sample Output : 
# 2 6
# 


# Solution:


a = input()
u = 0
l = 0
for x in a:
  if x.isupper():
    u+=1
  elif x.islower():
    l+=1
  else:
    pass
print(u,l)