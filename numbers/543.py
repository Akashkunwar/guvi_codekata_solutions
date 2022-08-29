# QID: 543
# 
# You are given a very long integer.Your task is to determine the smallest possible number such that sum of factorial of digits results back in n. Print -1 if no number is possible
# 
# You are given a number ‘n’
# 
# 
# Print the smallest number
# 
# 
# Sample Input : 
# 145
# 
# 
# Sample Output : 
# 145
# 
# 


# Solution:


n = int(input())
s =''
while(True):
    k = 1
    i = 1
    while(k<=n):
        k = k*i 
        i = i+1 
    k = k//(i-1)
    s = s+str(i-2)
    n= n-k
    if n == 0:
        break 
print(s[::-1])