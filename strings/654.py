# QID: 654
# 
# You are given a string s which is in compressed form. Your task is to expand the string and then print it.
# 
#  given a string ‘s’
# 
# expand the string and print it.
# 
# Sample Input : 
# 3(abc2(a))
# 
# Sample Output : 
# abcaaabcaaabcaa
# 
# 


# Solution:


b = list(input())[::-1]
d = ''
e = -1
for x in b:
  e=e+1
  if x.isalpha():
    d = d+x
  elif x.isdigit():
    d = d*int(x)
print(d[::-1])