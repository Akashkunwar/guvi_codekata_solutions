# QID: 670
# 
# You are given a string s. Your task is to tell whether string is beautiful or not.A beautiful string is a string in which String starts with a or A and middle element is either m or M and last element is zor Z
# 
#  
# 
# You are given a string ‘s’.
# 
# 
# Print 1 if string is beautiful and 0 if it is not
# 
# 
# Sample Input : 
# Amz
# 
# 
# Sample Output : 
# 1
# 


# Solution:


a = input()
b = int((len(a)+1)/2)
if a[0]=="a" or a[0]=="A":
  if a[-1]=="z" or a[-1]=="Z":
    if a[b-1]=="m" or a[b-1]=="M":
      print(1)
    else:
      print(0)
  else:
    print(0)
else:
  print(0)