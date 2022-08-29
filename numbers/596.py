# QID: 596
# 
# You are given an array of digits. Your task is to print the digit with maximum frequency.
# 
# You are given length of array ’n’,next line contains n space separated numbers. 
# 
# 
# Print the number with maximum frequency. If two number have equal freqency prin the number that comes first
# 
# 
# Sample Input : 
# 7
# 1 2 3 4 4 4 5
# 
# 
# Sample Output : 
# 4
# 


# Solution:


a = input()
test_list = [str(i) for i in input().split(" ")]
res = max(set(test_list), key = test_list.count)
print (str(res))