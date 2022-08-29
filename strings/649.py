# QID: 649
# 
# Write a program to get a string S, Type of conversion (1 - Convert to Lowercase, 2 - Convert to Uppercase) T, and integer P . Convert the case of the letters in the positions which are multiples of P.(1 based indexing).
# 
# Given a string S, Type of conversion  T, and integer P
# 
# Convert the case of the letters and print the string
# 
# Sample Input : 
# ProFiLe
# 1
# 2
# 
# 
# Sample Output : 
# Profile
# 
# 


# Solution:


a = input()
T = int(input())
P = int(input())
arr = []
for i in a:
    arr.append(i)
if T == 1:
    for i in range(1, int(len(a)/P)+1):
        arr[(P*i)-1] = arr[P*i-1].lower()
if T == 2:
    for i in range(1, int(len(a)/P)+1):
        arr[(P*i)-1] = arr[P*i-1].upper()
for i in arr:
    print(i, end='')