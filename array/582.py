# QID: 582
# 
# You are given an array of non-negative integers representing height of walls at index i as Ai and the width of each block is 1. Compute how much air can be encapsulated between the walls of chamber.
# 
#  
# 
# Each line contains an integer ‘N’ denoting the size of the array Next line contains N space separated numbers to be stored in array.
# 
# Output the total unit of Air encapsulated between the walls of chamber.
# 
# 
# Sample Input : 
# 3
# 7 4 9
# 
# 
# Sample Output : 
# 3
# 


# Solution:


nos = int(input())
numlist = list(map(int, input().split()))
lower = numlist[0]
if numlist[nos-1] < lower:
    lower = numlist[nos-1]
air_in = 0 
for ele in numlist[1:nos-1]:
    if ele < lower:
        air_in += lower - ele 
print(air_in)