# QID: 240
# 
# Given a number n followed by n numbers. Find the numbers which are equal to their index value and print them in sorted order. If no such numbers are present print '-1' without quotes.
# Input Size : 1 <= n <= 100000
# Sample Testcases :
# INPUT
# 6
# 6 7 3 3 4 5
# OUTPUT
# 3 4 5
# 
# 
# 
# 


# Solution:


a = input()
c = [int(i) for i in input().split(' ')]
i = -1
d = []
for x in c:
  i = i+1
  if i==x:
    d.append(x)
if len(d)==0:
    print(-1)
else:
    print(*d)