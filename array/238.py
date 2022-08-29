# QID: 238
# 
# Given a number N followed by N numbers. Find the largest number which can be formed from the given numbers and print it.
# NOTE: Each number should be used exactly once.
# Input Size : 1 <= N <= 100000 
# Sample Testcases :
# INPUT
# 5
# 5 6 7 8 9
# OUTPUT
# 98765
# 
# 
# 
# 


# Solution:


aaa = input()
def findMaxNum(arr, n):
	hash = [0] * 10
	for i in range(n):
		hash[arr[i]] += 1
	for i in range(9, -1, -1):
		for j in range(hash[i]):
			print(i, end = "")
if __name__ == "__main__":		
	arr = [int(i) for i in input().split(" ")]
	n =len(arr)
	findMaxNum(arr,n)