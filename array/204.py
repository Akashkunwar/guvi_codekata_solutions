# QID: 204
# 
# Given a number N and array of N integers, find the number which occurs the least number of times.
# Input Size : |N| <= 1000000
# 
# 
# Sample Testcase :
# INPUT
# 5
# 3 3 4 4 7
# OUTPUT
# 7
# 
# 
# 
# 


# Solution:


# Python 3 program to find the least
# frequent element in an array.


def leastFrequent(arr, n) :

	# Sort the array
	arr.sort()

	# find the min frequency using
	# linear traversal
	min_count = n + 1
	res = -1
	curr_count = 1
	for i in range(1, n) :
		if (arr[i] == arr[i - 1]) :
			curr_count = curr_count + 1
		else :
			if (curr_count < min_count) :
				min_count = curr_count
				res = arr[i - 1]
			
			curr_count = 1
			

	# If last element is least frequent
	if (curr_count < min_count) :
		min_count = curr_count
		res = arr[n - 1]
	
	return res
	
aaa = input()
# Driver program
arr = [int(i) for i in input().split(" ")]
n = len(arr)
print(leastFrequent(arr, n))


# This code is contributed
# by Nikita Tiwari.
