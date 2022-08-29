# QID: 508
# 
# Ria is a 5 year old girl. Her mother wants to teach her how to sort words in the same order that they appear in a dictionary. She decides to write a program to sort a given set of strings based on their alphabetical order. Help Rias mother to complete the program.
# 
#  
# 
# A set of N strings
# 
# 
# Alphabetically sorted set of strings
# 
# 
# Sample Input : 
# 3
# InfinityWar EndGame Avengers
# 
# Sample Output : 
# Avengers EndGame InfinityWar
# 


# Solution:


a = input()
b = input().split()
b.sort()
print(' '.join(b))