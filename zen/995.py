# QID: 995
# 
# Given a number n followed by n numbers add the odd number in an array
# 
# 0<n<100
# Given a number n 
# Followed by n number in next line
# 
# Print the sum of odd numbers in an array
# 
# Sample Input : 
# 6
# 5 7 4 4 6 8
# 
# Sample Output : 
# 12
# 


# Solution:


a = input()
b = [int(i) for i in input().split()]
c = 0
for x in b:
    if x%2!=0:
        c = c+x
    else:
        pass
print(c)