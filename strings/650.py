# QID: 650
# 
# Given a string 'S' print the sum of weight of the String. A weight of character is defined as the ASCII value of corresponding character.
# 
# You are given a  string ‘s’
# 
# 
# 
# Print weight
# 
# 
# Sample Input : 
# abc
# 
# 
# Sample Output : 
# 294
# 
# 


# Solution:


a = input()
words = list(a)
ascii = []
for word in words:
    for ch in word:
        ascii.append(ord(ch))
ascii = [ord(ch) for word in words for ch in word]
print(sum(ascii))