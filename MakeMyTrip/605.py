# QID: 605
# 
# Ramesh is searching a solution to problem posted. The statement is as follows
# 
# Print the maximum sum produced by increasing subarray. Ramesh is very confused to see the question,Help him.
# 
# You are given a number ‘n’,Then next line contains n space separated numbers.
# 
# 
# Maximum sum value produced by the increasing sub array of size 'n'
# 
# 
# Sample Input : 
# 6
# 2 1 4 7 3 6
# 
# 
# Sample Output : 
# 12
# 


# Solution:


aa = input()
a = [int(i) for i in input().split()]
b = 0
c = a[0]
for x in range(0,len(a)):
  try:
    if a[x]>a[x+1]:
      if c<b:
        c = b
      else:
        pass
      b = 0
      b = a[x+1]
      # print(b)
    elif a[x] < a[x+1]:
      b = b+a[x+1]
    else:
      pass
  except:
    pass
print(c)