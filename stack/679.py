# QID: 679
# 
# A string containing the prefix expression is given to you.Evaluate it and print the single integer giving the answer.
# 
# You are given a string ‘s’.
# 
# Print the evaluated answer of that string
# 
# Sample Input : 
# +23
# 
# 
# Sample Output : 
# 5
# 


# Solution:


a = input()
c = a[1:]
try:
    if a[0]=='+':
      b = int(c[0])+int(c[1])
    elif a[0]=='-':
      b = int(c[0])-int(c[1])
    elif a[0]=='*':
      b = int(c[0])*int(c[1])
    elif a[0]=='+':
      b = int(c[0])/int(c[1])
    print(b)
except:
    print(0)