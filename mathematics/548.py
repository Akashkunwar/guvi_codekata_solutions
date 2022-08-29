# QID: 548
# 
# In a garage the service man takes 10 minutes to service one car.If there are N cars in garage and X is number of minutes after which one person arrives,Calculate how much time last person has to wait in garage.(Print answer in minutes)
# 
# You are given Two numbers ‘N’ and  ‘X’
# 
# 
# Waiting time of last person
# 
# 
# Sample Input : 
# 4 5
# 
# 
# Sample Output : 
# 15
# 
# 


# Solution:


x,y = map(int,input().split())
print((x-1)*10-(x-1)*y)