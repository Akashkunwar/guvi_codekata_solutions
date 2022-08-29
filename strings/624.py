# QID: 624
# 
# Indian PAN card issuing authority have found some fake PAN cards. They have hired you so that you can validate PAN card for them. Your task is to develop a suitable algorithm which could check if pan is valid or not
# 
# 1)Pan must have uppercase letters only.
# 
# 2)It must be of 10 character only
# 
# 3)From index 1 to 5 all must be letters(A-Z),last index must be letter
# 
# 4)Rest all must be integer Starting from 1
# 
# You are given a input string which indicates the PAN number
# 
# 
# Print 'pan' if it is valid PAN number, else print 'not pan'
# 
# Sample Input : 
# HXTPS2142R
# 
# 
# Sample Output : 
# pan
# 
# 


# Solution:


import re
email = input()
regex = r"[A-Z][A-Z][A-Z][A-Z][A-Z][0-9][0-9][0-9][0-9][A-Z]"
if not re.search(regex,email):
  print("not pan")
else:
  print("pan")