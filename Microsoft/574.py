# QID: 574
# 
# You are given a number n,ranging from 1 to n. Out of which one number is missing. Your task is to print that missing number.
# 
#  
# 
# 
# 
# You are given a number ‘n’.
# 
# 
# Print the missing number.
# 
# 
# Sample Input : 
# 5
# 1 3 5 2
# 
# 
# Sample Output : 
# 4
# 


# Solution:


def getMissingNo(A):
	n = len(A)
	total = (n + 1)*(n + 2)/2
	sum_of_A = sum(A)
	return total - sum_of_A
aa = input()
A = [int(i) for i in input().split(" ")]
miss = getMissingNo(A)
print(int(miss))
