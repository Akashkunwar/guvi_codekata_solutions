# QID: 277
# 
# Given a number N followed by an array of N numbers. Another number D is given. Rotate the array D times and print the array.
# Input Size : N <= 100000, D<=100000
# 
# 
# Sample Testcase :
# INPUT
# 4 1
# 3 2 4 1
# OUTPUT
# 2 4 1 3
# 
# 
# 
# 


# Solution:


a,b = map(int, input().split(" "))
lia = [int(i) for i in input().split(" ")]
def rotate(l, n):
    return l[n:] + l[:n]
c = rotate(lia, b)
print(*c)