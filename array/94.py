# QID: 94
# 
# Given 2 numbers N and K.Print the number of occurrences of K in N.If K is not found print '-1'.
# Input Size : 1 <= N <= 100000, 0 <= K <= 9
# 
# 
# Sample Testcase :
# INPUT
# 1000 0
# OUTPUT
# 3
# 
# 
# 
# 


# Solution:


a,b = map(int, input().split(" "))
c = [str(d) for d in str(a)]
e = [int(i) for i in c]
f = e.count(b)
if f==0:
  print(-1)
else:
  print(f)