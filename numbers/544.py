# QID: 544
# 
# You are given a number n.Your task is to develop an algorithm to tell whether the number is ajs or not.An ajs number is a number whose sum of first two digits is present in given number n
# 
# A number ’n’ is given to you
# 
# 
# Print 1 if number is ajs or 0 if it is not
# 
# 
# Sample Input : 
# 9817
# 
# 
# Sample Output : 
# 1
# 


# Solution:


a = input()
n = int(a[0]) + int(a[1])
if str(n) in a:
    print(1)
else:
    print(0)