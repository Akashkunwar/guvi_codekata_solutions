# QID: 602
# 
# You are given with an array of numbers, Your task is to print the difference of indices of largest and smallest number.All number are unique.
# 
# First line contains a number ‘n’. Then next line contains n space separated numbers.
# 
# 
# Print the difference of indices of largest and smallest array
# 
# 
# Sample Input : 
# 5
# 1 6 4 0 3
# 
# 
# Sample Output : 
# -2
# 


# Solution:


aa = input()
a = [int(i) for i in input().split(" ")]
b=a.index(max(a))
c=a.index(min(a))
print(b-c)