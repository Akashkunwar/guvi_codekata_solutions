# QID: 589
# 
# You are provided with an array in which all elements are repeated thrice except one which is repeated twice.Your task is to print that number.
# 
#  
# 
# O(n) time and O(1) extra space
# 
# First line contains a number denoting size of array ‘n’.Next line contains n space separated numbers
# 
# 
# Print the number which is repeated twice
# 
# 
# Sample Input : 
# 5
# 13 12 13 12 13
# 
# 
# Sample Output : 
# 12
# 


# Solution:


a = input()
arr = list(map(int,input().split()))
c = []
for i in arr:
    if arr.count(i) == 2:
        if i not in c:
            
            c.append(i)
if len(c) >= 1:
    print(*c)