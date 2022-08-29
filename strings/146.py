# QID: 146
# 
# Find the word having maximum length in a given sentence and print it. If two words are of same length return the first occuring word of max-length.
# Input Size : |s| <= 100000
# 
# 
# Sample Testcase :
# INPUT
# guvi geek
# OUTPUT
# guvi
# 
# 
# 
# 


# Solution:


a,b=map(str,input().split(" "))
c = len(a)
d = len(b)
if c>d:
  print(a)
elif d>c:
  print(b)
else:
  print(a)