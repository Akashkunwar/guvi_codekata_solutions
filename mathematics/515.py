# QID: 515
# 
# Sreelatha was confused with series. She is given with a number n. There is a pattern hidden the series. She has to understand and print  the series till nth number by looking into example.Sreelatha is confused and She hired you , you have to develop the series for sreelatha by observing the pattern from the below example.
# 
#  She is given with a number ‘n’.
# 
#  print  the series till nth number 
# 
# Sample Input : 
# 3
# 
# 
# Sample Output : 
# 1 9 36
# 
# 


# Solution:


b = int(input())
c = []
for x in range(1,b):
  c.append(x)
d = [element * 3 for element in c]
d.insert(0, 1)
def square(list):
    return [i ** 2 for i in list]
a = square(d)
print(*a,sep=" ")