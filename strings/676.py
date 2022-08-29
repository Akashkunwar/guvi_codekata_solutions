# QID: 676
# 
# You are given some words all in lower case letters your task is to print them in sorted order.
# 
# You are given a string ‘s’
# 
# Print the string in sorted order
# 
# Sample Input : 
# virat kohli
# 
# Sample Output : 
# kohli virat
# 


# Solution:


a = [str(i) for i in input().split(" ")]
print(*sorted(a))