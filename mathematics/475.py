# QID: 475
# 
# You are given with a string which comprises of some numbers. Your task is to find the largest integer by converting the string to the corresponding integer.
# 
# First line contains n denoting number of Test Cases. The first and only Line of testcase has the string
# 
# Print the largest number
# 
# Sample Input : 
#  I was born on 12 october 1998.
# 
# Sample Output : 
# 1998
# 


# Solution:


a = [str(i) for i in input().split(" ")]
b = []
for i in a:
  i = i.replace(".","")
  i = i.replace(",","")
  if i.isdigit()==True:
    b.append(int(i))
  else:
    pass
print(max(b))