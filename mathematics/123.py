# QID: 123
# 
# Given a number N,check whether it has repeating digits in it.print 'yes' if it has repeating digits otherwise print 'no'.
# 
# 
# Sample Testcase :
# INPUT
# 11234
# OUTPUT
# yes
# 
# 
# 
# 


# Solution:


def countRepeatingDigits(N):
	res = 0
	cnt = [0] * 10
	while (N > 0):
		rem = N % 10
		cnt[rem] += 1
		N = N // 10
	for i in range(10):
		if (cnt[i] > 1):
			res += 1
	return res
N = int(input())
M = countRepeatingDigits(N)
if M==0:
  print("no")
else:
  print("yes")