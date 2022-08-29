# QID: 549
# 
# You are given with a number n. You have to count the pair of two numbers a and b such that sum of two numbers are equal to n.
# 
#  
# 
# Note:Both numbers lie in range 1<=a,b<n
# 
# You are given a number ‘n’
# 
# 
# Print the number of pairs satisfying above condition
# 
# 
# Sample Input : 
# 5
# 
# Sample Output : 
# 4
# 


# Solution:


a = int(input())
count = 0
for i in range(1,a):
    for j in range(1,a):
        if i+j == a:
            count += 1
print(count)
