# QID: 863
# 
# <strong>Radix sort</strong> is one of the sorting algorithms used to sort a list of integer numbers in order. In radix sort algorithm, a list of integer numbers will be sorted based on the digits of individual numbers. Sorting is performed from <strong>least significant digit to the most significant digit.</strong>
# 
# <strong><img alt="" src="https://s3.ap-south-1.amazonaws.com/guvi-2.0/codekata/qid863.png" style="height:192px; width:400px" /></strong>
# 
# You have to sort the given array of integer values in  radix sorting manner.
# 
# Given an integer 'n' which indicates the length of array and followed by space separated ‘n’ integer values.Where 1<=n<=100 and 100<=A[i]<=999.
# 
# Print the resultant sorted array by using radix sort method.where 100<=A[i]<=999.
# 
# Sample Input : 
# 8
# 189 678 234 567 892 121 123 125
# 
# Sample Output : 
# 121 123 125 189 234 567 678 892
# 


# Solution:


a = input()
b = [int(i) for i in input().split()]
b = sorted(b)
print(*b)