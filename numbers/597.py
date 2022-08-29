# QID: 597
# 
# you are given with array of numbers.you have to find whether array is beautiful or not. A beautiful array is an array whose sum of all numbers is divisible by 2, 3 and 5
# 
# You are given a number ‘n’ denoting the size of array.Next line contains n space separated numbers.
# 
# 
# Print 1 if array is beautiful and 0 if it is not
# 
# 
# Sample Input : 
# 5
# 5 25 35 -5 30
# 
# 
# Sample Output : 
# 1
# 


# Solution:


a = int(input())
arr = list(map(int,input().split()))
if sum(arr)%2 == 0 and sum(arr)%3 == 0 and sum(arr)%5 == 0:
    print(1)
else:
    print(0)