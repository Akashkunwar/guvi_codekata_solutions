# QID: 343
# 
#  Given k sorted arrays of possibly different sizes, merge them and print the sorted output.
# Input Size : N<=100 
# Example:
# INPUT
#  k = 3
# 1 3
# 2 4 6
# 0 9 10 11
# OUTPUT
# 0 1 2 3 4 6 9 10 11
# 
# 
# 
# 


# Solution:


a = input()
a = int(a[-1])
b = []
for x in range(0,a):
  c = [int(i) for i in input().split()]
  b = b+c
b = sorted(b)
print(*b)