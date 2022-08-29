# QID: 635
# 
# You are given with an array. For each element present in the array your task is to print the next smallest than that number. If it is not smallest print -1
# 
# You are given a number ‘n’ representing size of array. And n space separated numbers.
# 
# Print the next smallest number present in array and -1 if no smallest is present
# 
# Sample Input : 
# 7
# 10 7 9 3 2 1 15
# 
# 
# Sample Output : 
# 7 3 3 2 1 -1 -1
# 


# Solution:


a = int(input())
c = []
arr = list(map(int,input().split()))
for i in range(a):
    value = 0
    for j in range(i, a):
        if arr[i] >  arr[j]:
            value = arr[j]
            break 
        else:
            value = -1 
    c.append(value)
print(*c)