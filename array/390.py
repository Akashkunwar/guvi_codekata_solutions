# QID: 390
# 
# Vasanth is working at GUVI. He has been taking leave often in the past couple of weeks and his manager, who also happens to be his friend, is worried that Vasanth might be exceeding his number of paid holidays, which might be a black mark in Vasanth monthly report. The manager analysis Vasanths attendance register and decides to warn him beforehand. The attendance register has a P marked for present and an A marked for absent. Vasanth will be blacklisted if his attendance falls below 25%. Your task is to help the manager find out whether Vasanth could be blacklisted or not.
# 
#  
# 
# First line contains the number of entries in the attendance register, followed by space separated values of attendance (‘P’ or ‘A’)
# 
# 
# ‘Blacklisted’ if attendance is below 25%
# ‘Not Blacklisted’ if attendance is above 25%
# 
# 
# Sample Input : 
# 5
# P P A A A
# 
# 
# Sample Output : 
# Not Blacklisted
# 
# 


# Solution:


a = int(input())
b = [i for i in input().split()]
ab = b.count('P')
at = ab/len(b)
if at>.25:
    print('Not Blacklisted')
else:
    print('Blacklisted')