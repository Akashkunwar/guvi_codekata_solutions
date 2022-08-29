# QID: 586
# 
# You are given with an circular array .Your task is calculate the difference between two consecutive number. And if difference is greater than k, print 1 else print 0
# 
# You are given two numbers ‘n’, ’m’. Next line contains n space separated integers.
# 
# 
# Print 1 if the difference is greater than ‘m’.
# 
# 
# Sample Input : 
# 5 15
# 50 65 85 98 35
# 
# 
# Sample Output : 
# 0 1 0 1 0
# 
# 


# Solution:


n, k = map(int,input().split())
a = list(map(int,input().split()))
arr = []
for i in range(n-1):
    if abs(a[i]-a[i+1]) > k:
        arr.append(1)
    else:
        arr.append(0)
arr1= a[-1]-a[0] 
if abs(arr1) > k:
    arr.append(1)
else:
    arr.append(0)
print(*arr)