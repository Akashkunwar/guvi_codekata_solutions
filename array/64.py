# QID: 64
# 
# Given a string S consisting of a sentence, the task is to reverse every word of the sentence except the first and last character of the words.
# 
# 
# Sample Testcase :
# INPUT
# guvi coding platform
# OUTPUT
# gvui cnidog proftalm.
# 
# 
# 
# 


# Solution:


a = [str(i) for i in input().split(" ")]
b = []
def rev(a):
  b.append(a[0]+a[1:-1][::-1]+a[-1])

for x in a:
  if len(x)==1:
    b.append(x)
  else:
    rev(x)

print(*b)