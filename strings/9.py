# QID: 9
# 
# Given a string S, print it after changing the middle element to * (if the length of the string is even, change the 2 middle elements to *).
# 
# 
# Sample Testcase :
# INPUT
# hello
# OUTPUT
# he*lo
# 
# 
# 
# 


# Solution:


a = input()
b = len(a)
a = list(a)
if (b%2==0):
  g = int(b/2)
  h = int(g+1)
  a[g-1:h] = "**"
  a = "".join(a)
  print(a)
else:
  c = int((b+1)/2)
  a[c-1] = "*"
  a = "".join(a)
  print(a)