# QID: 485
# 
# Dityan is alloted with a task. He is provided with some positive numbers. He has to tell the smallest positive natural number(greater than the minimum number present in the list) and in addition to it,the number should not be present in the list and it should not be equal to the sum of any combination of n numbers present in the list.You have to develop a suitable program in order to find that number m.
# 
# First line contains a number ‘n’ . next line contains ‘n’ space separated numbers.
# 
# 
# print the smallest positive number ‘m’.
# 
# 
# Sample Input : 
# 5
# 1 2 10 12 13
# 
# 
# Sample Output : 
# 4
# 


# Solution:


a = int(input())
arr = list(map(int, input().split()))
s = []
for i in range(a):
    for j in arr[:i]:
        #if arr[i] != j:
        s.append(arr[i]+j)
lst = list(range(1,10))
for i in lst:
    if i not in s and i not in arr and i > min(arr):
        print(i)
        break