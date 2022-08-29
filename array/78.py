# QID: 78
# 
# Given a number N and an array of N strings, find the number of strings that are an anagram of 'kabali'.If there exists no anagram for the given string print '0'.
# Input Size : 1 <= N <= 1000
# 
# 
# Sample Testcase :
# INPUT
# 5
# kabali
# kaabli
# kababa
# kab
# kabail
# OUTPUT
# 3
# 
# 
# 
# 


# Solution:


a = int(input())
b = 0
c = []
while b<a:
  c.append(input())
  b+=1
d = []
for x in c:
  if ''.join(sorted(list(x))) in ''.join(sorted(c[0])):
    d.append(1)
  else:
    d.append(0)
if sum(d)==1:
    print(0)
else:
    print(sum(d))