# QID: 994
# 
# Given a number n followed by n numbers add the even number in an array
# 
# 0<n<100
# Given a number n 
# Followed by n number in next line
# 
# Print the sum of even numbers in an array
# 
# Sample Input : 
# 6
# 5 7 4 4 6 8
# 
# Sample Output : 
# 22
# 


# Solution:


a = input()
b = [int(i) for i in input().split()]
c = 0
for x in b:
    if x%2==0:
        c+=x
    else:
        pass
print(c)