# QID: 1004
# 
# Given a string find the number of special characters if their no special characters print -1
# 
# Given a string
# 
# Print number of special characters or -1
# 
# Sample Input : 
# Guvi Geek
# 
# Sample Output : 
# -1
# 


# Solution:


a = input()
b = 0
for x in a:
  if x.isalpha() == False and x.isdigit() == False and x != ' ':
    b = b+1
  else:
    pass
if b>0:
  print(b)
else:
  print(-1)