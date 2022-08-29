# QID: 981
# 
# Given a number n print the three prime number which comes next to number n
# 
# 0<n<100
# Given a number n
# 
# print the three  prime number which comes next to number n
# 
# Sample Input : 
# 3
# 
# Sample Output : 
# 5 7 11
# 


# Solution:


a = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]
b = int(input())
a.append(b)
a = list(set(a))
c = a.index(b)
d = a[c+1:c+4]
print(*d)