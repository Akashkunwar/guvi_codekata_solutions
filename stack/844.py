# QID: 844
# 
# Given two strings S1 and S2. The task is to find if a string &#39;S2&#39; can be obtained by rotating another string &#39;S1&#39; by 2 places using <strong>Stack</strong>.
# 
# The first line of the input contains the string S1.
# The second line of the input contains the string S2
# 
# 
# Print 1 if the string S2 can be obtained by rotating string S1 by two places else print 0.
# 
# Sample Input : 
# amazon
# azonam
# 
# Sample Output : 
# 1
# 


# Solution:


def isRotated(str1, str2):
	if (len(str1) != len(str2)):
		return False
	if(len(str1) < 2):
		return str1 == str2
	clock_rot = ""
	anticlock_rot = ""
	l = len(str2)
	anticlock_rot = (anticlock_rot + str2[l - 2:] +
									str2[0: l - 2])
	clock_rot = clock_rot + str2[2:] + str2[0:2]
	return (str1 == clock_rot or
			str1 == anticlock_rot)
if __name__ == "__main__":
	str1 = input()
	str2 = input()
if isRotated(str1, str2):
	print(1)
else:
	print(0)