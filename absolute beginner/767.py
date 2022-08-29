# QID: 767
# 
# You are given three numbers <strong>A</strong>, <strong>B</strong> &amp; <strong>C</strong>. Print the largest amongst these three numbers.
# 
# Three numbers are provided to you.
# 
# Find and print the largest among the three
# 
# Sample Input : 
# 1
# 2
# 3
# 
# Sample Output : 
# 3
# 


# Solution:


A = int(input())
B = int(input())
C = int(input())
if (A>B) and (A>C):
    print(A)
elif (B>A) and (B>C):
    print(B)
else:
    print(C)