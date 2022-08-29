# QID: 151
# 
# Given a number N and an array of N integers, find the smallest number divisible by all the elements of the array.
# Input Size : N <= 100000
# 
# 
# Sample Testcase :
# INPUT
# 5
# 1 2 3 4 5
# OUTPUT
# 60
# 
# 
# 
# 


# Solution:



def __gcd(a, b):
    if (a == 0):
        return b
    return __gcd(b % a, a)
def LcmOfArray(arr, idx):
    if (idx == len(arr)-1):
        return arr[idx]
    a = arr[idx]
    b = LcmOfArray(arr, idx+1)
    return int(a*b/__gcd(a,b))
aa = input()
arr = [int(i) for i in input().split(" ")]
print(LcmOfArray(arr, 0))