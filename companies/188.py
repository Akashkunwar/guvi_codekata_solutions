# QID: 188
# 
# Given a sentence interchange the between the word 'and'.
# Input Size : |S| <= 1000000 
# 
# 
# Sample Testcase :
# INPUT
# jack and jill went up and down to get water
# OUTPUT
# jill and jack went down and up to get water
# 
# 
# 
# 


# Solution:


a = [str(i) for i in input().split(" ")]

t = -1
for x in a:
  t = t+1
  if x == 'and':
    b = a[t-1]
    c = a[t+1]
    a[t-1] = c
    a[t+1] = b

print(*a)