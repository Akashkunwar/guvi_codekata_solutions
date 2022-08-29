# QID: 479
# 
# Shreya is a brilliant girl. She likes to memorize the numbers. These numbers will be shown to her. As an examiner develop an algorithm to test her memory.
# 
#  
# 
# CONSTRAINTS
# 
# 1<=Y,N,T<=1000
# 
# First line contains no. of test cases(Y). Next line contains a number N. Next line contains n space separated numbers
# Next line contains a number T denoting the number of questions asked from you regarding the given array.
# Next line contains T space separated numbers.
# 
# 
# Print the occurrence of each number if present else “NOT PRESENT”
# 
# Sample Input : 
# 10
# 1 1 1 2 2 2 3 8 9 7
# 5
# 1 2 3 0 5
# 
# 
# Sample Output : 
# 3 3 1 Not Present Not Present
# 


# Solution:


a = input()
b = [int(i) for i in input().split()]
c = input()
d = [int(i) for i in input().split()]
e = []
for x in d:
  f = b.count(x)
  if f==0:
    e.append('Not Present')
  else:
    e.append(f)
print(*e)