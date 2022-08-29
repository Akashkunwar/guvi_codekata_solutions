# QID: 85
# 
# Given an array of N strings sort it in ascending order based on the length of the string.If two strings are found to have the same length sort them in lexicographical order.
# 
# 
# Sample Testcase :
# INPUT
# 3
# coding platform codekata
# OUTPUT
# coding codekata platform
# 
# 
# 
# 


# Solution:


aa = input()
a = [i for i in input().split()]
a.sort()
b = []
for x in a:
  b.append(len(x))
dic = dict(zip(a,b))
sorted_dt = {key: value for key, value in sorted(dic.items(), key=lambda item: item[1])}
d = list(sorted_dt.keys())
c = []
for x in d:
  c.append(x)
print(*c)