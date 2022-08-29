# QID: 547
# 
# In XYZ country there is rule that cars engine no. depends upon car number plate. Engine no is sum of all the integers present on cars Number plate.The issuing authority has hired you in order to provide engine no. to the cars.Your task is to develop an algorithm which takes input as in form of string(Number plate) and gives back
# 
# Engine number.
# 
# You are given a string ’s’
# 
# 
# Print the engine number
# 
# 
# Sample Input : 
# HR05-AA-2669
# 
# 
# Sample Output : 
# 28
# 
# 


# Solution:


a = input()
r = 0
for i in a:
    if i in ('1234567890'):
        r = int(i)+r 
    else:
        continue 
print(r)