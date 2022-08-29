# QID: 677
# 
# Guvi developed a new system to make sure no two usernames are same. So, they hired you as a developer to develop this system. They have set some rules to do the same.If you see the same username that already exists, just add a number at the end of that username ,else print &quot;Verified&quot;.
# 
# First line consists of an integer N, denoting number of usernames. Second line consists of N spaced separated Strings, denoting usernames.
# 
# print the required output in a new line.
# 
# Sample Input : 
# 4
# abc aab abc aba
# 
# Sample Output : 
# Verified Verified abc1 aba
# 
# 


# Solution:


aa = input()
a = [str(i) for i in input().split(" ")]
b = []
c = []
for x in a:
  if x in b:
    c.append(x+"1")
  else:
    b.append(x)
    c.append("Verified")
print(*c)