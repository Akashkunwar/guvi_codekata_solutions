# QID: 623
# 
# You are provided with a string s. Your task is to reverse the string using stack Data Structure.
# 
#  
# 
# You are given a string ‘s’.
# 
# 
# Print the reverse string 
# 
# 
# Sample Input : 
# i am jsb
# 
# 
# Sample Output : 
# jsb am i
# 
# 


# Solution:


a = [str(i) for i in input().split(' ')]
print(*a[::-1])