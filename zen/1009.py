# QID: 1009
# 
# Given a string reverse the words in the string
# 
# Given a string
# 
# Print string into reverse the words in the string
# 
# 
# 
# Sample Input : 
# guvi geek
# 
# Sample Output : 
# ivug keeg
# 


# Solution:


a = [i for i in input().split()]
b = []
for x in a:
  b.append(x[::-1])
print(*b)