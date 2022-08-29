# QID: 701
# 
# You are given string s. Your task is to modify the string as mentioned below:-
# 
# 1)The string should not have three consecutive same characters.
# 
# 2)You can add any number of characters anywhere in the string. Find the minimum number of characters which Ishaan must insert in the string.
# 
# You are given a string ‘s’
# 
# print the required answer in a new line.
# 
# Sample Input : 
# aabbbcc
# 
# Sample Output : 
# 1
# 


# Solution:


a = input()
arr = []
condition = 0
for i in a:
    arr.append(i)
for i in range(len(a)-2):
    if arr[i] == arr[i+1] and arr[i] == arr[i+2]:
        condition += 1
print(condition)