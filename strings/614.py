# QID: 614
# 
#  <span style="font-size:14px">Radha newly learnt about palindromic strings.A palindromic string is a string which is same when read from left to right and also from right to left.Help her in implementing the logic.</span> 
# 
# You are given a String ‘s’ 
# 
# 
# Print 1 if String is palindrome or 0 if not
# 
# 
# Sample Input : 
# NITIN
# 
# 
# Sample Output : 
# 1
# 


# Solution:


a = str(input())
b = a[::-1]
if (a == b):
  print(1)
else:
  print(0)