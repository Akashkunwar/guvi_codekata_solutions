# QID: 779
# 
# You are provided with two numbers. Find and print the smaller number.
# 
# You are provided with two numbers as input.
# 
# Print the small number out of the two numbers.
# 
# Sample Input : 
# 23 1
# 
# Sample Output : 
# 1
# 


# Solution:


a,b = map(int, input().split(" "))
if (a<b):
    print(a)
else:
    print(b)