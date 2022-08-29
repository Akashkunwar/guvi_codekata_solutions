# QID: 652
# 
#  You are given a true string. String is called true if weight of string is multiple of 8. Your task is to tell whether a string can be declared True or Not. Weight of string is the sum of ASCII value of Vowel character(s) present in the string.
# 
# You are given as string ‘s’ in lower cases
# 
# Print 1 for true and 0 for false
# 
# Sample Input : 
# raja
# 
# Sample Output : 
# 0
# 


# Solution:


b = input()
aa = sum([ord(a) for a in b])
if aa%8==0:
  print(1)
else:
  print(0)