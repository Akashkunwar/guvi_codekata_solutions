# QID: 541
# 
# you are given with arasu series(shown in example).You have to understand it and you will be given a number n ,you have to print the series till n numbers.
# 
# You are given a number n;
# 
# 
# Print series till nth number
# 
# 
# Sample Input : 
# 4
# 
# 
# Sample Output : 
# 2 5 10 17
# 
# 
# 


# Solution:


N = int(input())
x = [2]
y = 3
for i in range(1,N):
    a = x[i-1]+y
    x.append(a)
    y+=2
print(*x)