# QID: 265
# 
# Write a program to give the following output for the given string S of size N.(character containing even number of occurences should be elaborated else print the same format)
# Eg 1: Input: a1b10
# Output: a1bbbbbbbbbb
# Eg: 2: Input: b3c6d15
# Output: b3ccccccd15
# Input Size : 1 <= N <= 100000
# Sample Testcases :
# INPUT
# a1b10
# OUTPUT
# a1bbbbbbbbbb
# 
# 
# 
# 


# Solution:


import re

a = input()

x = re.findall('\D', a)
y = re.findall('\d+', a)
c = ''
for s,t in zip(x,y):
  if int(t)%2==0:
    c = c+s*int(t)
  else:
    c = c+s+t  
print(c)