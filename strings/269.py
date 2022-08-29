# QID: 269
# 
# Given a sequence of strings remove extra spaces in the string(there can be atmost one space between 2 strings).
# Input Size : 1<= N <= 100000 
# Sample Testcases :
# INPUT
# aa   abba abba
# OUTPUT
# aa abba abba
# 
# 
# 
# 


# Solution:


a = [str(i) for i in input().split(" ")]
for x in a:
  if x=='':
    a.remove('')
print(*a)