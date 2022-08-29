# QID: 25
# 
# Find the minimum among 10 numbers.
# 
# 
# Sample Testcase :
# INPUT
# 5 4 3 2 1 7 6 10 8 9
# OUTPUT
# 1
# 
# 
# 
# 


# Solution:


a,b,c,d,e,f,g,h,i,j = map(int, input().split(" "))
k = [a,b,c,d,e,f,g,h,i,j]
print(min(k))