# QID: 609
# 
# harish learnt about gcd and and want to apply the concept to find the gcd of n numbers.
# 
# But in between he got stuck and now he is asking for some help your task is to print the gcd of n numbers and print -1 if there is no gcd possible
# 
#  
# 
# You are given an array size ‘n’.Next line contains n space separated numbers.
# 
# 
# Your task is to print the gcd of number
# 
# 
# Sample Input : 
# 6
# 2 4 8 16
# 
# 
# Sample Output : 
# 2
# 


# Solution:


def find_gcd(x, y):
	
	while(y):
		x, y = y, x % y
	
	return x
aa = input()
l = [int(i) for i in input().split(" ")]

num1 = l[0]
num2 = l[1]
gcd = find_gcd(num1, num2)

for i in range(2, len(l)):
	gcd = find_gcd(gcd, l[i])
print(gcd)