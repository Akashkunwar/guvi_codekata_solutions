
# You are given a number N and followed by an array of N numbers and followed by two elements U and V, find the minimum distance between the elements in the array. The array may have duplicates.
# For example, if the array is (1, 5, 3, 7, 2, 8, 3, 4, 5, 9, 9, 3, 1, 3, 2, 9)
# Min Distance (U=4, V= 7): 4
# Input Size : N <= 100000

# Sample Testcase :

# INPUT
# 16
# 1 5 3 7 2 8 3 4 5 9 9 3 1 3 2 9
# 4 7

# OUTPUT
# 4

# Solution

a = input()
a = [int(i) for i in input().split()]
b,c = map(int, input().split())
indices = [i for i, x in enumerate(a) if x == b]
indices1 = [i for i, x in enumerate(a) if x == c]
l = []
for x in indices:
  for y in indices1:
    l.append(abs(x-y))
print(min(l))