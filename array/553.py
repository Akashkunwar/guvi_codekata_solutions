# QID: 553
# 
# You are a passport issuer, but due to some problems in the system, there are redundant  passport numbers. Your task is to delete all the duplicate passport numbers. You are given a list of passport numbers.
# 
# You are given length of list.Second line,You are given with a list.
# 
# 
# Print the list of passport numbers without duplicates.
# 
# 
# Sample Input : 
# 5
# A23 B56 B56 C79 D16
# 
# 
# Sample Output : 
# A23 B56 C79 D16
# 
# 


# Solution:


a = int(input())
arr = list(map(str,input().split()))
c = []
for i in arr:
    if i not in c:
        c.append(i)
print(*c)