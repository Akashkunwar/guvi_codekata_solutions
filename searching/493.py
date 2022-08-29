# QID: 493
# 
# Ramesh is a  student and wants to find out if there is any other student in his class who has got the same marks as his, in maths. Help him to find out.
# 
#  
# 
# First line contains the number of students in the class followed by Ramesh’s mark. Second line contains the marks of all students in the class.
# 
# 
# Index of student who got mark same as Ramesh’s mark. If no such mark exists, return -1.
# 
# 
# Sample Input : 
# 2 10
# 1 2
# 
# 
# Sample Output : 
# -1
# 


# Solution:


a,b = map(int,input().split())
c = [int(i) for i in input().split(" ")]
try:
  print(c.index(b))
except:
  print(-1)