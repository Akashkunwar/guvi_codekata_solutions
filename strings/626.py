# QID: 626
# 
# Shriti was going through some cryptographic concept. She just got stuck at some place . She needs your help to sort out the situation. Your task is to help her in writing the decrypted string.
# 
#  
# 
# The first line of the input consists of a Encrypted string input
# 
# Print the decrypted string, by analysing the logic behind the decryption using the sample input and output.
# 
# Sample Input : 
# 3[b[2[aa]]]
# 
# 
# Sample Output : 
# baaaabaaaabaaaa
# 


# Solution:


a = input()
a = list(a)
b = []
for x in a:
  if x == '[' or x == ']':
    pass
  else:
    b.append(x)
b = b[::-1]
c = ''
for x in b:
  if x.isdigit():
    c = c*int(x)
  elif x.isalpha():
    c = c+x
print(c[::-1])