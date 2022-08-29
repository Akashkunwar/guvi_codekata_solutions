# QID: 687
# 
# You are given an array of numbers. Print the least occurring element. If there is more than 1 element print all of them in decreasing order of their value.
# 
# You are given a number ‘n’ denoting size of array. Next line contains n space separated numbers.
# 
# Print the number as mentioned
# 
# Sample Input : 
# 9
# 1 6 4 56 56 56 6 4 2
# 
# 
# Sample Output : 
# 2 1
# 


# Solution:


def getAllindex(lst, elem):
     return list(filter(lambda a: lst[a] == elem, range(0,len(lst))))
aaa = input()
lst = [int(i) for i in input().split(" ")]

list_count = [lst.count(xx) for xx in lst]
idx = getAllindex(list_count, min(list_count))

l = list(set([lst[ii] for ii in idx]))
l.sort(reverse = True)
print(*l, sep = " ")