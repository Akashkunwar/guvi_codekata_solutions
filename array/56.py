# QID: 56
# 
# Given an array of N elements which follows either even number or odd number series.There may exists at maximum 1 even number in the odd series or 1 odd number in the even series.Find the different number if exists otherwise print '-1'?
# Input Size : |N| <= 100000
# 
# 
# Sample Testcase :
# INPUT
# 5
# 1 3 4 5 7
# OUTPUT
# 4
# 
# 
# 
# 


# Solution:


a = input()
b = [int(i) for i in input().split()]
even = []
odd = []

for x in b:
    if x%2==0:
        even.append(x)
    else:
        odd.append(x)

if len(even)==1:
    print(even[0])
elif len(odd)==1:
    print(odd[0])
else:
    print(-1)