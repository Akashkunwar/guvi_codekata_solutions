# QID: 599
# 
# Rahul was learning about numbers in list. He came across one word ground of a number.
# 
# A ground of a number is defined as the number which is just smaller or equal to the number given to you.Hence he started solving some assignments related to it. He got struck in some questions. Your task is to help him.
# 
#  
# 
# O(n) time complexity
# 
# O(n) Auxilary space
# 
# First line contains two numbers ‘n’ denoting number of integers and ‘k’ whose ground is to be check. Next line contains n space separated numbers.
# 
# 
# Print the index of val.Print -1 if equal or near exqual number 
# 
# 
# Sample Input : 
# 7 3
# 1 2 3 4 5 6 7
# 
# 
# Sample Output : 
# 2
# 


# Solution:


a,k = map(int,input().split())
arr = list(map(int,input().split()))
lst = [i for i in arr if i <= k]
lst.sort(reverse = True)
print(arr.index(lst[0]))