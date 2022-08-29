# QID: 474
# 
# Rajesh and Ram are having a conflict on the maximum marks that they have scored in all the exams conducted in the past year. The one having scored the maximum gets a treat from the other. They decide to go through their test papers and record their highest marks. You are Rajeshs best friend and as he has tutions to attend, he gives you all his test papers and asks you to find out the maximum marks that he has scored among all the marks in all exams. He promises you a treat if he wins the bet with Ram. Help Rajesh find out his highest marks.
# 
# Constraints:
# 
# 1 <= N <= 10
# 
# 0 <= A[] <= 100
# 
# First line contains count of marks. Next line is the list of marks obtained by Rajesh.
# 
# Highest marks obtained by Rajesh.
# 
# Sample Input : 
# 3
# 82 96 72
# 
# 
# Sample Output : 
# 96
# 


# Solution:


a = int(input())
n = [int(i) for i in input().split(" ")]
print(max(n))