# QID: 555
# 
# Assume that you are ticket verifier at a club. Your club has decided to give a special discount to the person(s) who are satisfying the following condition
# 
#  
# 
# Condition:-
# 
# If ticket number is divisible by date of month. You are eligible for a discount.
# 
# First line contains input ‘n’.Next line contains n space separated numbers denoting ticket numbers .Next line contains ‘k’ date of the month.
# 
# 
# Print  1 if the ticket is eligible for discount else 0
# 
# 
# Sample Input : 
# 6
# 112 139 165 175 262 130
# 22
# 
# 
# Sample Output : 
# 0 0 0 0 0 0
# 
# 


# Solution:


n = int(input())
a = list(map(int,input().split()))
b = int(input())
for i in range(0,n):
    if(a[i]%b == 0):
        a[i]=1
    else:
        a[i]=0
print(*a)