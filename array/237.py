# QID: 237
# 
# Given a number N, check if the sum of the digits is a Palindrome. Print 'yes' or 'no' accordingly.
# Input Size : 2 <= N <= 1000000000000000000 
# Sample Testcases :
# INPUT
# 13
# OUTPUT
# yes
# 
# 
# 
# 


# Solution:


def digitSum(n) :

	sum = 0;
	while (n > 0) :
		sum += (n % 10);
		n //= 10;

	return sum;
def isPalindrome(n) :
	divisor = 1;
	while (n // divisor >= 10) :
		divisor *= 10;

	while (n != 0) :
		leading = n // divisor;
		trailing = n % 10;
		if (leading != trailing) :
			return False;
		n = (n % divisor) // 10;
		divisor = divisor // 100;

	return True;
def isDigitSumPalindrome(n) :
	sum = digitSum(n);

	if (isPalindrome(sum)) :
		return True;
	return False;

if __name__ == "__main__" :

	n = int(input());

	if (isDigitSumPalindrome(n)) :
		print("yes");
	else :
		print("no");