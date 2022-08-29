# QID: 88
# 
# Given a string/sentence remove all the spaces and print the result.
# Input Size : |s| <= 1000000(complexity O(n))
# 
# 
# Sample Testcase :
# INPUT
# guvi  geeks
# OUTPUT
# guvigeeks
# 
# 
# 
# 


# Solution:


a = list(input())
b = []
for x in a:
  if x!=" ":
    b.append(x)
  else:
    pass
print(*b,sep=(""))