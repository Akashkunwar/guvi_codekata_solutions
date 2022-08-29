# QID: 611
# 
# You are given given task is to print whether array is majestic or not.A majsetic array is an array whose sum of first three number is equal to last three number.
# 
# You are given a number ‘n’,Next line contains ‘n’ space separated 
# 
# 
# Print 1 if array is majestic and 0 if it is not
# 
# 
# Sample Input : 
# 7
# 1 2 3 4 6 0 0
# 
# 
# Sample Output : 
# 1
# 


# Solution:


aa = input()
a = [int(x) for x in input().split(" ")]
b = sum(a[:3])
c = sum(a[-3:])
if b==c:
  print(1)
else:
  print(0)