# QID: 203
# 
# Let P represent Paper, R represent Rock and S represent Scissors. Given 2 out of the 3 determine which one wins. If its a draw print 'D'.
# 
# 
# Sample Testcase :
# INPUT
# R P
# OUTPUT
# P
# 
# 
# 
# 


# Solution:


a,b = map(str, input().split(" "))
if a=="R" and b=="P":
  print("P")
elif a=="P" and b=="S":
  print("S")
elif a=="R" and b=="S":
  print("D")
elif a=="P" and b=="R":
  print("P")
elif a=="S" and b=="P":
  print("S")
elif a=="S" and b=="R":
  print("R")
else:
  print("D")