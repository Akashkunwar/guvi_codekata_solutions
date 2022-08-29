# QID: 231
# 
# Given a number N, find the smallest number which is greater than N with the same digits in N. If N is the greatest digit print 'impossible'.
# Input Size : 1 <= N <= 1000000000000000000
# Sample Testcases :
# INPUT
# 123
# OUTPUT
# 132
# 
# 
# 
# 


# Solution:


def findNext(number,n):
	for i in range(n-1,0,-1):
		if number[i] > number[i-1]:
			break
	if i == 1 and number[i] <= number[i-1]:
		print ('impossible')
		return
	x = number[i-1]
	smallest = i
	for j in range(i+1,n):
		if number[j] > x and number[j] < number[smallest]:
			smallest = j
	number[smallest],number[i-1] = number[i-1], number[smallest]
	x = 0
	for j in range(i):
		x = x * 10 + number[j]
	number = sorted(number[i:])
	for j in range(n-i):
		x = x * 10 + number[j]
	
	print (x)
digits = input()		
number = list(map(int ,digits))
findNext(number, len(digits))
