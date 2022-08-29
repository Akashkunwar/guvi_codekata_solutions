# QID: 179
# 
# Given a string and a number K, change every kth character to uppercase from beginning in string.
# 
# 
# Sample Testcase :
# INPUT
# string 2
# OUTPUT
# sTrInG
# 
# 
# 
# 


# Solution:


a,b = input().split()
a = list(a)
b = int(b)
try:
  c = list(range(0,len(a)+1,b))
  for x in c:
    a[x]=a[x].upper()

  print(*a,sep="")
except:
  print(*a,sep="")