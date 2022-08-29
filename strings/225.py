# QID: 225
# 
# Given a string 'S', sort the characters based on the frequency(highest and lowest) and print the resultant string.(Note:If the frequency of different character is same then sort based on alphabetical order).
# Input Size : 1 <= S <= 100000
# Sample Testcases :
# INPUT
# aabbba
# OUTPUT
# aaabbb
# 
# 
# 
# 


# Solution:


from collections import Counter
a = input()
a = list(a)
a = Counter(a)
sorted_dict = {k: v for k, v in sorted(a.items(), key=lambda item: item[1])}

k = list(sorted_dict.keys())
v = list(sorted_dict.values())

b = ''
for x,y in zip(k,v):
  b = b + x*y
b = b
print(b)