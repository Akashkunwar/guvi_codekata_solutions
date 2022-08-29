# QID: 321
# 
#  Given a string S convert each characters of the string  into ASCII values and print the sum of the numbers.
# Input Size : |s| <= 100000 
# 
# 
# Sample Testcase :
# INPUT
# guvi
# OUTPUT
# 443
# 
# 
# 
# 


# Solution:


words = list(input())
ascii = []
for word in words:
    for ch in word:
        ascii.append(ord(ch))
ascii = [ord(ch) for word in words for ch in word]
print(sum(ascii))