# QID: 664
# 
#  You are given a string s.Your task is to print the string in alternate lowercase and uppercase order.
# 
# You are given a string
# 
# Print the string according to given criteria
# 
# Sample Input : 
# abcd efgh ijkl
# 
# Sample Output : 
# ABCD efgh IJKL
# 


# Solution:


a = [str(i) for i in input().split(" ")]
l = len(a)
cap = list(range(0,l,2))
for x in cap:
  a[x] = a[x].upper()
print(*a)