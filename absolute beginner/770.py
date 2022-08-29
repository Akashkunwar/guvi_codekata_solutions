# QID: 770
# 
# You are provided with a number check whether its odd or even. 
# 
# Print &quot;Odd&quot; or &quot;Even&quot; for the corresponding cases.
# 
# Note: In case of a decimal, Round off to nearest integer and then find the output. Incase the input is zero, print &quot;Zero&quot;.
# 
# A number is provided as the input.
# 
# Find out whether the number is odd or even.
# Print "Odd" or "Even" for the corresponding cases.
# Note: In case of a decimal, Round off to nearest integer and then find the output. In case the input is zero, print "Zero".
# 
# Sample Input : 
# 2
# 
# Sample Output : 
# Even
# 


# Solution:


a = int(input())
if a%2 == 0:
  print("Even")
else:
  print("Odd")