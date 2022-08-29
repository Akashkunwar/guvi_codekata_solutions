# QID: 628
# 
#  Joseph was going through topic of strings. He learnt about anagrams. But due to some circumstances he forget ,now he hired you to help him in completing the work.Your task is to tell whether the two given strings are anagrams
# 
# The first line of the input is a string N, the second line of the input is a string M
# 
# Compare the two string input N and M. Print 1 if they are anagram else print 0.
# 
# 
# Sample Input : 
# abcd
# cdab
# 
# 
# Sample Output : 
# 1
# 


# Solution:


a = input()
b = input()
if len(a)==len(b):
  a = list(set(list(a)))
  b = list(set(list(b)))
  if a==b:
    print(1)
  else:
    print(0)
else:
    print(0)