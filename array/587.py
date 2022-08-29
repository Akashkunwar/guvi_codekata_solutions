# QID: 587
# 
# You are given with an array. Your task is to print the left rotated array after k opearations.
# 
# Time:O(n)
# 
# Extra Space: O(1)
# 
# First line contains two number ‘n’ and ‘k’.Next line contains n space separated numbers.
# 
# 
# Print the array as mentioned.
# 
# 
# Sample Input : 
# 7 3
# 1 2 3 4 5 6 7
# 
# 
# Sample Output : 
# 4 5 6 7 1 2 3
# 
# 


# Solution:


b,c = map(int,input().split(" "))
a = [int(i) for i in input().split(" ")]
for x in range(c):
    a = a[1:]+[a[0]]
print(*a)