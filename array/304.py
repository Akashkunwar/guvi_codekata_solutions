# QID: 304
# 
#  Given a number N print a right angled traingle structure with the starting level as single 1 and every immediate proceeding level with 2 more additional ones than the previous level .Repeat the pattern for N levels.
# Input Size : N <= 1000
# 
# 
# Sample Testcase :
# INPUT
# 3
# OUTPUT
# 1
# 1 1 1
# 1 1 1 1 1
# 
# 
# 
# 


# Solution:


N = int(input())
k = '1'
for i in range(N):
    print(k)
    k += ' 1 1'
