# QID: 103
# 
# Given 2 strings.check if the second string is a substring of the first string.Print 'yes' if there exists a valid substring otherwise print 'no'.
# Input Size : 1 <= N <= 100000
# 
# 
# Sample Testcase :
# INPUT
# codekata code
# OUTPUT
# yes
# 
# 
# 
# 


# Solution:


a,b = input().split()
if b in a:
  print("yes")
else:
  print("no")