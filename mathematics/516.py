# QID: 516
# 
# Assume your brother studies in class 2. He has to  complete his homework on co-primes. As an elder sibling help him in finding whether the given two numbers is co-prime or not.
# 
# You will be given two numbers ‘n’ and ‘m’
# 
# 
# Your task is to tell whether numbers is co prime or not. If it is a co-prime print 1 else 0
# 
# 
# Sample Input : 
# 3 5
# 
# 
# Sample Output : 
# 1
# 
# 


# Solution:


def __gcd(a, b):
	if (a == 0 or b == 0): return 0
	if (a == b): return a
	if (a > b):
		return __gcd(a - b, b)
	return __gcd(a, b - a)
def coprime(a, b):
	if ( __gcd(a, b) == 1):
		print(1)
	else:
		print(0)	
a,b = map(int,input().split(" "))
coprime(a, b)