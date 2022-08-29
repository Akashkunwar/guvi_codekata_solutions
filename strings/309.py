# QID: 309
# 
# Given 2 strings P,Q of length N,M generate a password from two strings by combining corresponding index letter of each string.If the any one string is less than the other then numbers starting from1,2,3.... are taken to equate the length of the strings.
# Explanation:If the strings are Abi & Bhuvana then the password is ABbhiu1v2a3n4a-
# Input Size : 1 <= N, M <= 100000
# 
# 
# Sample Testcase :
# INPUT
# Vishal Yadav
# OUTPUT
# VYiasdhavl1
# 
# 
# 
# 


# Solution:


a, b = input().split() 

if len(a)>len(b):
  c = len(a) - len(b)
  d = []
  for x in range(1,c+1):
    d.append(x)

elif len(a)<len(b):
  c = len(b) - len(a)
  d = []
  for x in range(1,c+1):
    d.append(x)

else:
  pass

e = ''
for x in d:
  e = e+str(x)

if len(a)>len(b):
  b = b+e
elif len(a)<len(b):
  a = a+e
else:
  pass

f = ''
for x,y in zip(a,b):
  f = f+x+y
  
print(f)