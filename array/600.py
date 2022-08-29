# QID: 600
# 
# You are given two arrays of equal length. Your task is to merge the two arrays then sort them too and then find the sum of two middlemost elements.
# 
# You are given a number ‘n’. Then Next line contains first list of 'n' separated numbers.Third line contains second list of 'n' space separated numbers.
# 
# 
# Print the sum of two middle elements
# 
# 
# Sample Input : 
# 5
# 1 9 16 25 46
# 2 3 4 5 6
# 
# 
# Sample Output : 
# 11
# 


# Solution:


aa = input()
a = [int(i) for i in input().split(" ")]
b = [int(i) for i in input().split(" ")]
c = a+b
c = sorted(c)
c1 = c[int(len(c)/2)-1]
c2 = c[int(len(c)/2)]
print(c1+c2)