# QID: 539
# 
# You are given a set of numbers, out of which you have to tell which of them are finest. A finest number n is a number which is formed by a number t such that
# 
# n=t^3+(t+1)^3
# 
#  
# 
# t is a natural number
# 
# You are given a number ‘z’ representing total numbers in an array, Next line contains z space separated numbers.
# 
# 
# Print the numbers which are finest in ascending order if there are no such numbers print -1.
# 
# 
# Sample Input : 
# 2
# 1729 189
# 
# 
# Sample Output : 
# 189 1729
# 
# 


# Solution:


a = int(input())
arr = list(map(int, input().split()))
lst = []
form = 1
for i in arr:
    for j in range(1,100+1):
        form = j**3 + (j+1)**3 
        if i == form:
            lst.append(i)
lst.sort()
print(*lst)