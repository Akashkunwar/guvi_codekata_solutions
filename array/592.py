# QID: 592
# 
# In a cricket match the coach wanted to check the performance of batsmen o he decided strike rate as criteria. He planned that the two batsmen whose strike rate difference minimum will be sent no. 3 and no.4 in next match.Now your task is to help the coach in finding the two batsmen.
# 
#  
# 
# You are given an integer ’n’ denoting the size of array. Next line contains n space separated integers. 
# 
# 
# Print the strike rate of two batsmen in same order of their occurence
# 
# Sample Input : 
# 6
# 138.3 156.5 156.6 160.2 198.3 146.2
# 
# 
# Sample Output : 
# 156.5 156.6
# 
# 


# Solution:


ss = input()
a = [float(i) for i in input().split()]
z = 100000
aa = ''
bb = ''
for x in a:
  for y in a:
    if x-y!=0:
      if abs(x-y)<z:
        z=abs(x-y)
        aa = x
        bb = y
      else:
        pass
    else:
      pass
print(aa,bb)