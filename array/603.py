# QID: 603
# 
# In a world cup tournament,no of goals scored by each team is given to you. Your task is to calculate net goal rate of each team.
# 
# Net goal rate of team is calculated
# 
#  
# 
# No of goals(team)- sum of(no of goals by last 3 teams)
# 
# You are given a number ‘n’.Next line contains n space separated numbers.
# 
# 
# Print the net goal rate of each team
# 
# 
# Sample Input : 
# 5
# 95 85 75 12 11
# 
# 
# Sample Output : 
# -3 -13 -23 -86 -87
# 


# Solution:


a = int(input())
b = [int(i) for i in input().split()]
l = sum(b[-3:])
c = []
for x in b:
    c.append(x-l)
print(*c)