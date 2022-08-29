# QID: 577
# 
# You are given an array of ids of prisoners. The jail authority found that there are some prisoners of same id. Your task is to help the authority in finding the common ids.
# 
# First line contains a number ‘n’ representing no of prisoners. Next line contains n space separated numbers.
# 
# 
# 
# Print the ids which are not unique. Print -1 if all ids are unique
# 
# 
# Sample Input : 
# 7
# 1 1 11 121 131 141 98
# 
# 
# Sample Output : 
# 1
# 


# Solution:


a = input()
arr= list(map(int,input().split()))
c_id = []
for i in arr:
    if arr.count(i) >= 2:
        if i not in c_id:
            c_id.append(i)
if len(c_id) >= 1:
    print(*c_id)