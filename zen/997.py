# QID: 997
# 
# Given a number n and m followed by n numbers remove the number m in the n number and print the remaining n number if m is not found print -1
# 
# 0<n<100
# Given a number n 
# Followed by n number in next line
# 
# Print the remaining numbers or -1
# 
# Sample Input : 
# 6 43
# 5 7 4 4 6 8
# 
# Sample Output : 
# -1
# 


# Solution:


a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
if a[1] in b:
    b.remove(a[1])
    print(*b)
else:
    print(-1)