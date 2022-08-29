# QID: 684
# 
# Given a string S consisting of lowercase latin letters, arrange all its letters in lexographical order using Counting Sort.
# 
# First Line contains positive integer N denoting the length of string.The second line of input contains the string S.
# 
# Print the sorted string.
# 
# Sample Input : 
# 5
# edsab
# 
# Sample Output : 
# abdes
# 


# Solution:


aa = input()
a = [str(i) for i in input()]
a.sort()
print(*a,sep='')