# QID: 494
# 
# Ram is the CEO of an MNC. He wants to order the employee salaries in ascending order so that he can do a salary hike based on the salary values of employees. He selects you to do the task of sorting the salaries. Sort the salaries in ascending order and pass on the information to Ram.
# 
#  
# 
# Number of employees followed by the salaries of employees.
# 
# 
# Salaries sorted in ascending order.
# 
# 
# Sample Input : 
# 8
# 7000 8000 6500 1200 4000 2800 3000 5230
# 
# 
# Sample Output : 
# 1200 2800 3000 4000 5230 6500 7000 8000
# 
# 


# Solution:


a = input()
b = [int(i) for i in input().split()]
b = sorted(b)
print(*b)