# QID: 601
# 
# Rajesh was going through alternative array sorting. He wishes to print the array alternatively. Hence hired you. Your task is to help rajesh in printing the array alternatively.
# 
# An alternative array is an array in which first element is maximum of the whole array second element is minimum of the whole array. Third element is the second largest. Fourth element is the second smallest And so on. print the array in the desired manner.
# 
# 
# You are given with the length of array ‘n’. followed by  ‘n’ space separated numbers.
# 
# 
# Print the array as mentioned.
# 
# 
# Sample Input : 
# 5 1 7 11 16 19
# 
# 
# Sample Output : 
# 19 1 16 7 11
# 
# 


# Solution:


a = input()
a = [int(i) for i in input().split()]
# a = aa[1:]
b = sorted(a)
c = b[::-1]
d = []
for x,y in zip(c,b):
  d.append(x)
  d.append(y)
print(*d[:len(a)])