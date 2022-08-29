# QID: 688
# 
# Pk finds it difficult to judge the minimum element in the list of elements given to him. Your task is to develop the algorithm in order to find the minimum element.
# 
#  Note:Dont use sorting
# 
#  
# 
# You are given ‘n’ number of elements. Next line contains n space separated numbers.
# 
# Print the minimum element
# 
# Sample Input : 
# 5
# 3 4 9 1 6
# 
# 
# Sample Output : 
# 1
# 


# Solution:


aa = input()
a = [int(i) for i in input().split(" ")]
print(min(a))