# QID: 17
# 
# Given a string S, print 2 strings such that first string containing all characters in odd position(s) and other containing all characters in even position(s).
# 
# 
# Sample Testcase :
# INPUT
# XCODE
# OUTPUT
# XOE CD
# 
# 
# 
# 


# Solution:


a = input()
b = list(range(1,len(a),2))
c = list(range(0,len(a),2))
even = ""
for x in c:
  even = even+a[x]
odd = ""
for x in b:
  odd = odd+a[x]
print(even,odd)