# QID: 665
# 
# You are given a string.Your task is to print only the consonants present in the string without affecting the sentence spacings if present. If no consonants are present print -1
# 
# You are given a string ‘s’.
# 
# 
# Print only consonants.
# 
# 
# 
# Sample Input : 
# I am shrey 
# 
# Sample Output : 
#  m shry
# 


# Solution:


a = str(input())
if ("a" or "e" or "i" or "o" or "u") in a:
  b = a.replace("a","")
  c = b.replace("e","")
  d = c.replace("i","")
  e = d.replace("o","")
  f = e.replace("u","")
  g = f.replace("I","")
  h = g.replace("A","")
  i = h.replace("E","")
  j = i.replace("O","")
  k = j.replace("U","")
  print(k)
else:
  print(a)