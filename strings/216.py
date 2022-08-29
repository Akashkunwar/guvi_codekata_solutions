# QID: 216
# 
# Given a string print reverse all words except the first and last words.
# 
# 
# Sample Testcase :
# INPUT
# Hi how are you
# OUTPUT
# Hi woh era you
# 
# 
# 
# 


# Solution:


a = list(input().split())
for x in range(1,len(a)-1):
  a[x] = a[x][::-1]
print(*a)