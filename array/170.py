# QID: 170
# 
# Given a number N and 2 arrays of N integers and their weights, sort the array based on their weights in the ascending order.
# Input Size : N <= 100000
# 
# 
# Sample Testcase :
# INPUT
# 5
# 1 2 3 4 5
# 5 4 3 2 1
# OUTPUT
# 5 4 3 2 1
# 
# 
# 
# 


# Solution:


a = int(input())
b = [int(i) for i in input().split()]
c = [int(i) for i in input().split()]
dic = dict(zip(b,c))
sorted_dict = dict(sorted(dic.items(),
                           key=lambda item: item[1],
                           reverse=True))
print(*list(sorted_dict.keys())[::-1])