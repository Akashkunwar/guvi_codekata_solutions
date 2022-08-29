# QID: 77
# 
# Given two numbers L,R print the smallest number which is divisible by both L and R.
# Input Size : 1 <= L,R <= 100000
# 
# 
# Sample Testcase :
# INPUT
# 10 130
# OUTPUT
# 130
# 
# 
# 
# 


# Solution:


def compute_lcm(x, y):
   if x > y:
       greater = x
   else:
       greater = y
   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1
   return lcm
num1,num2 = map(int,input().split(" "))
print(compute_lcm(num1, num2))