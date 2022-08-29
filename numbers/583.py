# QID: 583
# 
# Jack is fond of numbers. He has given an array.He has to find the maximum length of sub array such that sum of elements in that sub array gives output 0.He is in little trouble, help him in finding solution
# 
# You are given an integer ‘n’ denoting the number of elements in array.Next line contains n space separated integers
# 
# 
# Print the max length of that array with sum 0 and print -1 if not possible
# 
# 
# Sample Input : 
# 6
# -4 3 1 0 0 6
# 
# 
# Sample Output : 
# 5
# 


# Solution:


n = int(input())
arr = [int(x) for x in input().split()]
lst = []
for i in range(n):
    for j in range(i, n):
        a = []
        for k in range(i, j+1):
            a.append(arr[k])
        lst.append(a)
m = len(lst[0])
flag = False
for i in lst:
    if sum(i) == 0 and m < len(i):
        m = len(i)
        flag = True
if flag:
    print(m)
else:
    print(-1)