# QID: 853
# 
# Given a string A representing an absolute path for a file.Print the string A after simplifying the absolute path using <strong>Stack</strong>.
# 
# Given a string S contains the absolute path of file.
# 
# Print the string S after simplified absolute path of a file.
# 
# Sample Input : 
# C:/home/guvi
# 
# Sample Output : 
# /guvi
# 


# Solution:


a = input()
b = a[::-1]
c = b.index('/')
print(b[:c+1][::-1])