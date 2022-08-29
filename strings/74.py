# QID: 74
# 
# Given a string S, print the reverse of the string after removing the vowels.If the resulting string is empty print '-1'.
# Input Size : 1 <= N <= 100000
# 
# 
# Sample Testcase :
# INPUT
# codekata
# OUTPUT
# tkdc
# 
# 
# 
# 


# Solution:


a = input()[::-1]
b=a.replace("a","")
c=b.replace("e","")
d=c.replace("i","")
e=d.replace("o","")
f=e.replace("u","")
g=f.replace("A","")
h=g.replace("E","")
i=h.replace("I","")
j=i.replace("O","")
k=j.replace("U","")
if len(k)>0:
  print(k)
else:
  print(-1)