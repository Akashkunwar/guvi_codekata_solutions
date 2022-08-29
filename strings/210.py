# QID: 210
# 
# Given a string S ,print the vowels first and then consonants in the same order as they have occurred in the string.
# Input Size : N <= 10000
# 
# 
# Sample Testcase :
# INPUT
# GuVI
# OUTPUT
# uIGV
# 
# 
# 
# 


# Solution:


a = input()
b = []
c = []
for x in a:
  if x=='a'or x=='e'or x=='i'or x=='o'or x=='u' or x=='A'or x=='E'or x=='I'or x=='O'or x=='U':
    b.append(x)
  else:
    c.append(x)
d = b+c
print(*d,sep='')