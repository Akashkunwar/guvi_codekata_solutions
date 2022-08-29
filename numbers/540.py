# QID: 540
# 
# You are given a number n. You have to tell whether a number is great or not. A great number is a number whose sum of digits let (m) and product of digits let(j) when summed together gives the number back
# 
# m+j=n
# 
#  
# 
# You are given a number n;
# 
# 
# Print Great if a number is great else print the no 
# 
# 
# Sample Input : 
# 59
# 
# 
# Sample Output : 
# Great
# 
# 


# Solution:


a=int(input())
b=str(a)
c=int(b[0])
d=int(b[1])
e=c+d
f=c*d
g=e+f
if(a==g):
    print("Great")
else:
    print("no")