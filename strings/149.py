# QID: 149
# 
# Given a date(DD-MM-YYYY),print the month in words.
# 
# 
# Sample Testcase :
# INPUT
# 01-01-2018
# OUTPUT
# January
# 
# 
# 
# 


# Solution:


a,b,c=map(str,input().split("-"))
if b=="01":
  print("January")
elif b=="02":
  print("February")
elif b=="03":
  print("March")
elif b=="04":
  print("April")
elif b=="05":
  print("May")
elif b=="06":
  print("June")
elif b=="07":
  print("July")
elif b=="08":
  print("August")
elif b=="09":
  print("September")
elif b=="10":
  print("October")
elif b=="11":
  print("November")
elif b=="12":
  print("December")
else:
  pass