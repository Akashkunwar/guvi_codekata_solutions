# QID: 154
# 
# Given 2 strings S,X. Print the string after deleting X.If X not found print the same string.
# Input Size : 1 <= |s|, |x| <= 1000
# 
# 
# Sample Testcase :
# INPUT
# Happy Birthday
# Happy
# OUTPUT
# Birthday
# 
# 
# 
# 


# Solution:


b = [str(i) for i in input().split(" ")]
a = input()
try:
  b.remove(a)
except:
  pass
print(*b)