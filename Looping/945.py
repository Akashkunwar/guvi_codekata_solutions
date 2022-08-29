# QID: 945
# 
# Write a program to get a list of integers as input and find the LCM of the values without using GCD
# 
# First line contains an integer N, number of values.
# Second line contains N space separated values.
# 
# Print the LCM of the values.
# 
# Sample Input : 
# 1 2 3 4 5
# 
# Sample Output : 
# 60
# 


# Solution:


def LCM(arr, n):
	max_num = 0;
	for i in range(n):
		if (max_num < arr[i]):
			max_num = arr[i];
	res = 1;
	x = 2;
	while (x <= max_num):
		indexes = [];
		for j in range(n):
			if (arr[j] % x == 0):
				indexes.append(j);
		if (len(indexes) >= 2):
			for j in range(len(indexes)):
				arr[indexes[j]] = int(arr[indexes[j]] / x);
			res = res * x;
		else:
			x += 1;
	for i in range(n):
		res = res * arr[i];
	return res;
aaa = input()
arr = [int(i) for i in input().split(" ")];
n = len(arr);
print(LCM(arr, n));