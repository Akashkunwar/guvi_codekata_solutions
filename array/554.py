# QID: 554
# 
# You are given with two arrays. Your task is to merge the array such that first array is in ascending order and second one in descending order.
# 
# First line contains two integer ‘n’ and ‘m’. ‘n’ denotes length of array 1 and ‘m’ of array 2.Next line contains n space separated numbers and third line contains ‘m’ space separated numbers 
# 
# 
# Print a single array in desired order
# 
# 
# 
# Sample Input : 
# 3 3
# 23 15 16
# 357 65 10
# 
# 
# Sample Output : 
# 15 16 23 357 65 10
# 
# 


# Solution:


a =input()
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
arr1.sort()
arr2.sort(reverse = True)
c = arr1 + arr2 
print(*c)