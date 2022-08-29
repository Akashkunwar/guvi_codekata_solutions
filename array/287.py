# QID: 287
# 
# Given 2 numbers N and K and followed by an array of N integers. The given element K is removed from the array and new array is printed. If after removing every occurance of K the array becomes empty, print 'empty' without quotes.
# Example:
# Input: {10,10,20,30,76}, K=10
# Output: {20,20,76}
# Input Size : N <= 100000
# 
# 
# Sample Testcase :
# INPUT
# 5 10
# 10 10 20 30 76
# OUTPUT
# 20 30 76
# 
# 
# 
# 


# Solution:


a,b = map(int,input().split(" "))
a = [int(i) for i in input().split(" ")]
while True:
  b in a
  try:
    a.remove(b)
  except:
    break
if len(a)==0:
  print("empty")
else:
  print(*a)