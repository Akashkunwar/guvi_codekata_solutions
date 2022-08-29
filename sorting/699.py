# QID: 699
# 
# You are given a number n. Your task is to create the smallest number possible using the digits of number. The number should be of the same length as the orignal input number.
# 
# You are given a number ‘n’,
# 
# Print the smallest possible number of same length
# 
# Sample Input : 
# 123456789123456789
# 
# Sample Output : 
# 112233445566778899
# 


# Solution:


a = list(input())
if '0' not in a:
  a = list(map(int, a))
  a = sorted(a)
  print(*a,sep="")
else:
  b = []
  e = []
  c = list(map(int, a))
  c = sorted(c)
  a = list(map(int, a))
  for x in c:
    if x != 0:
      b.append(x)
      d = b[0]
      try:
        c.remove(d)
      except:
        pass
  e.append(d)
  e = e+c
  print(*e,sep='')