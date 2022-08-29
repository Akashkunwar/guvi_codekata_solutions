# QID: 42
# 
# Given 2 numbers N,X and an array of N elements, check if there exists any 2 numbers in the array with sum equal to X.If found print 'yes' otherwise print 'no'
# Input Size : N,X <= 100000
# 
# 
# Sample Testcase :
# INPUT
# 4 4
# 2 2 0 0
# OUTPUT
# yes
# 
# 
# 
# 


# Solution:


def chkPair(A, size, x) :
	for i in range (0, size - 1) :
		for j in range (i + 1, size):
			if (A[i] + A[j] == x) :				
				return True
	return False

y,x = map(int,input().split(" "))
A = [int(i) for i in input().split(" ")]
size = len(A)

if (chkPair(A, size, x)) :
	print("yes")
else :
	print("no")

