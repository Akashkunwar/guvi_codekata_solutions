# QID: 591
# 
# Ramit is given a list of both positive and negative integers. He has to tell the maximum sum out of all subarrays in the given list. He got confused and requested help from you. Now it is your task to find the maximum sum out of all subarrays in the given list.
# 
# You are given a number 'n'. Next line contains n space separated numbers.
# 
# 
# Print the max sum of subarray.
# 
# 
# Sample Input : 
# 5
# 1 2 3 -2 5
# 
# 
# Sample Output : 
# 9
# 


# Solution:


a = input()
b = [int(i) for i in input().split()]
c = sum(b)
if c>0:
    print(c)
else:
    print(-1)