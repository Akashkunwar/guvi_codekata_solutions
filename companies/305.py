# QID: 305
# 
#  Given a number 'N' print the sum of each digit to the power of number of digits in given input.
# Example :
# Input => 1234
# => ( 1 ^ 4 ) + ( 2 ^ 4 ) + ( 3 ^ 4 ) + ( 4 ^ 4 )
# => 1 + 16 + 81 + 256
# Output => 354
# N <=100000000000
# 
# 
# Sample Testcase :
# INPUT
# 1234
# OUTPUT
# 354
# 
# 
# 
# 


# Solution:


a = input()
b = []
for x in a:
  b.append(int(x)**len(a))
print(sum(b))