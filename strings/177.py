# QID: 177
# 
#  Given a string S. Find the maximum length of substring alternating characters of vowel and consonants.
# Input Size : |S| <= 1000000 
# 
# 
# Sample Testcase :
# INPUT
# bebibo
# OUTPUT
# 6
# 
# 
# 
# 


# Solution:


a = input()
if len(a)==1:
  print(0)
else:
  v = 0
  c = 0
  for x in a:
    if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
      v = v+1
    else:
      c = c+1

  # print('v',v)
  # print('c',c)

  max = v+c
  print(max)