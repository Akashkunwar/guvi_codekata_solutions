# QID: 686
# 
# You will be given an integer. Your task is to find the factorial of that big integer.
# 
# You are given an integer
# 
# Print  the factorial of that number
# 
# Sample Input : 
# 100
# 
# Sample Output : 
# 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
# 


# Solution:


a = int(input())
b = 1
for x in range(1,a+1):
  b = x*b
print(b)