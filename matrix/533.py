# QID: 533
# 
# The population of North Korea and South Korea are represented in a square matrix, with the upper triangular elements(including the diagonal) representing North Korea and lower Triangular elements(excluding the diagonal) representing South Korea. Kim Jong-un  asks you to inform him the current population figures of his country. Note: The elements are in a scale of 1000. 1 means 1000, 2 means 2000 and so on.
# 
#  
# 
# Dimensions of the matrix followed by the elements of the matrix
# 
# 
# Sum of upper triangular elements
# 
# 
# Sample Input : 
# 3 3
# 1 2 3
# 3.25 2 3
# 1.1 1 3
# 
# 
# Sample Output : 
# 14000
# 
# 


# Solution:


a,b = map(int, input().split())
arr = []
count = 0
ar = 0
for i in range(a):
    arr.append(list(map(float, input().split())))
for i in range(a):

    for j in range(0+ar, b):
        count += arr[i][j]
    ar += 1
print(int(count*1000))