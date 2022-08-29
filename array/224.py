# QID: 224
# 
# Given a string 'S' print the substring of maximum length which is not a palindrome.If more than one solution is possible print the solution which you obtained by performing elimination at the end of the string
# Input Size : 1 <= length <= 1000
# Sample Testcases :
# INPUT
# ababababa
# OUTPUT
# abababab
# INPUT
# hello
# OUTPUT
# hello
# 
# 
# 
# 


# Solution:


aa = input()
a = list(list(aa))
b = a[::-1]
if a==b:
  print(aa[:-1])
else:
  print(aa)