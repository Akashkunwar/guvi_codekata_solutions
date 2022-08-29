# QID: 943
# 
# Write a code get an integer number as input and print the odd and even digits of the number separately.
# 
# A single line containing an integer.
# 
# Print the even and odd integers of the integer in a separate line.
# 
# Sample Input : 
# 1234
# 
# Sample Output : 
# 2 4
# 1 3
# 


# Solution:


s=input()
l=[int(i) for i in s]
# print(l)
even = []
odd = []
for j in l:
  if j%2==0:
    even.append(j)
  else:
    odd.append(j)
print(" ".join(str(x) for x in sorted(even)))
print(" ".join(str(x) for x in sorted(odd)))