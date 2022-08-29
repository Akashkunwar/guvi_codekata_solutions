# QID: 1008
# 
# Given a string reverse the string
# 
# Given a string
# 
# Print string into reverse
# 
# Sample Input : 
# guvi geek
# 
# Sample Output : 
# geek guvi
# 


# Solution:


a = [i for i in input().split()]
a = a[::-1]
print(*a)