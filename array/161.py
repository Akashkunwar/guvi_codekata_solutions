# QID: 161
# 
# Given a number n and 2 numbers l and r followed by n numbers, find the smallest number in the range [l,r].
# 
# 
# Sample Testcase :
# INPUT
# 5 2 4
# 1 2 3 4 5
# OUTPUT
# 2
# 
# 
# 
# 


# Solution:


n,l,r = map(int, input().split(" "))
a = [int(i) for i in input().split(" ")]
b = list(range(l,r))
c = list(set(a).intersection(b))
c = sorted(c)
try:
  print(c[0])
except:
  print(sorted(a)[0])