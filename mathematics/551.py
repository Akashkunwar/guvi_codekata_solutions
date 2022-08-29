# QID: 551
# 
# Ajay is given a series(In example).he gone through the series but unable to understand it properly,he has hired you.Your task is to understand the series and print the series 2,6,12,20,30... .You are given with a number n. Find the nth number of series.
# 
# You are given a number ‘n’.
# 
# 
# Print the nth number of series
# 
# 
# Sample Input : 
# 5
# 
# Sample Output : 
# 30
# 


# Solution:


aa = []
f = int(input())
a = 2
for x in range(0,f):
  aa.append(a)
  a = a+2
b = [0]
for x in aa:
  b.append(x+b[-1])
print(b[-1])