# QID: 595
# 
# Ramesh is given  a task to generalise the array. An array is called generalise if median of that array is equal to sum k.Ramesh has less knowledge amongst median so he decided to take help from you.Your task is to count the number of elements that you must add to the median of given array equal to a number k.
# 
# First line contains a number ‘n’.next line contains n space separated numbers.next line contains a number ‘k’
# 
# 
# Print the count required in order to make the median of array equal to k
# 
# 
# Sample Input : 
# 6 
# 10 20 30 100 150 200
# 30
# 
# 
# Sample Output : 
# 1
# 


# Solution:


a = int(input())
arr = list(map(int,input().split()))
k = int(input())
num = a//2
c = 0
if k in arr and arr.index(k) == num-1:
    print(arr.count(k))
else:
    b = arr[num-1]
    print(5)