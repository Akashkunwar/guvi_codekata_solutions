# QID: 588
# 
# You are given with an array. Your task is to print the right rotated array after k operations.
# 
# Time:O(n)
# 
# Extra Space: O(1)
# 
#  
# 
# First line contains two number ‘n’ and ‘k’.Next line contains n space separated numbers.
# 
# 
# Print the array as mentioned.
# 
# 
# Sample Input : 
# 14 117
# 15 26 35 98 61 1230 75 96 63 21 1654 98654 320145 987
# 
# 
# Sample Output : 
# 21 1654 98654 320145 987 15 26 35 98 61 1230 75 96 63
# 
# 


# Solution:


b = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
for x in range(0,b[1]):
  a = [a[len(a)-1]] + a[:len(a)-1]
print(*a)