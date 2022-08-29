# QID: 528
# 
# Rohan is a coder who loves puzzles involving words and letters. He has recently learnt about the concept of matrices in mathematics and has developed a puzzle in a which a matrix of dimensions 5*5 is filled with letters of the English alphabet. Your task is to help Rohan in displaying the number of rows in which all the 5 vowels in the English alphabet are present.
# 
#  
# 
# Elements in the 5*5 matrix (a,b,c,d….z/A,B,C,D,...Z)
# 
# 
# Number of rows containing all the 5 vowels, distinctly. If there are no such rows, display 0.
# 
# 
# Sample Input : 
# A b c d e
# G h i j k
# L d M N o
# p Q R s t
# U V W x y
# 
# Sample Output : 
# 0
# 


# Solution:


arr = []
for i in range(5):
    arr.append(input().split())
b = 0 
for i in arr:
    a = [j for j in i]
    a.sort()
    a = ''.join(a)
    if a.lower() == 'aeiou':
        b += 1
print(b)