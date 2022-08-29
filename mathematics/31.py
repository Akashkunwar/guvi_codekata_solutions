# QID: 31
# 
# Given 2 numbers N,M. Find their difference and check whether it is even or odd.
# 
# 
# Sample Testcase :
# INPUT
# 5 5
# OUTPUT
# even
# 
# 
# 
# 


# Solution:


a,b = map(int,input().split(" "))
if a>b:
  e = a-b
  if e%2==0:
    print("even")
  else:
    print("odd")
elif b>a:
  e = b-a
  if e%2==0:
    print("even")
  else:
    print("odd")
else:
  print("even")